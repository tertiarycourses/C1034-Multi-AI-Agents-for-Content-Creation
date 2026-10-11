// node scripts/publish.mjs <id> [--live]
// Dry run by default: prints the exact request and sends nothing.
// --live posts ONE approved, unchanged, not-yet-published item.
import { readFileSync, statSync } from 'node:fs';
import { join } from 'node:path';
import { ROOT, readRows, readContent, liveBlocker, logPublish, loadEnv, mask, imageType } from './lib.mjs';

const [id, ...flags] = process.argv.slice(2);
const live = flags.includes('--live');
if (!id) { console.error('usage: node scripts/publish.mjs <id> [--live]'); process.exit(1); }

const row = readRows().find((r) => r.id === id);
if (!row) { console.error(`${id} is not in review/approvals.csv — run submit.mjs first.`); process.exit(1); }
if (live) {
  const why = liveBlocker(id);                  // defence in depth: the hook checks too
  if (why) { console.error(`REFUSED: ${why}`); process.exit(3); }
}
const { meta, body } = readContent(row.file);
const env = loadEnv();

// LinkedIn "little text": reserved characters must be escaped or the post is cut short.
// URLs are left as they are, so links keep working.
const littleText = (s) => s.split(/(https?:\/\/\S+)/).map((part, i) =>
  (i % 2 ? part : part.replace(/[\\|{}@[\]()<>#*_~]/g, (c) => `\\${c}`))).join('');

// The post's image (optional): `image:` and `alt:` in the frontmatter.
const image = meta.image ? { path: meta.image, type: imageType(meta.image), alt: meta.alt || '' } : null;
if (image && !image.alt) console.warn('WARNING: the image has no alt text (add "alt:" to the frontmatter).');
const imageBytes = () => readFileSync(join(ROOT, image.path));
const withLink = () => (meta.link && !body.includes(meta.link) ? `${body}\n\n${meta.link}` : body);

const liHeaders = (type = 'application/json') => ({ Authorization: `Bearer ${env.LINKEDIN_ACCESS_TOKEN}`,
  'LinkedIn-Version': env.LINKEDIN_VERSION || '202609', 'X-Restli-Protocol-Version': '2.0.0', 'Content-Type': type });

// LinkedIn image, step 1 of 2: register it and get an upload URL + image URN.
function linkedinImageInit() {
  return {
    method: 'POST', url: 'https://api.linkedin.com/rest/images?action=initializeUpload', headers: liHeaders(),
    body: JSON.stringify({ initializeUploadRequest: { owner: env.LINKEDIN_AUTHOR_URN } }),
    secret: env.LINKEDIN_ACCESS_TOKEN,
  };
}

// LinkedIn image, step 2 of 2: PUT the bytes to the upload URL.
function linkedinImageUpload(uploadUrl) {
  return {
    method: 'PUT', url: uploadUrl,
    headers: { Authorization: `Bearer ${env.LINKEDIN_ACCESS_TOKEN}`, 'Content-Type': image.type },
    body: imageBytes(), shown: `<${image.path}, ${statSync(join(ROOT, image.path)).size} bytes>`,
    secret: env.LINKEDIN_ACCESS_TOKEN,
  };
}

function linkedin(imageUrn) {
  const post = { author: env.LINKEDIN_AUTHOR_URN, commentary: littleText(withLink()), visibility: 'PUBLIC',
    distribution: { feedDistribution: 'MAIN_FEED', targetEntities: [], thirdPartyDistributionChannels: [] },
    lifecycleState: 'PUBLISHED', isReshareDisabledByAuthor: false };
  if (imageUrn) post.content = { media: { id: imageUrn, altText: image.alt } };
  return {
    method: 'POST', url: 'https://api.linkedin.com/rest/posts', headers: liHeaders(),
    body: JSON.stringify(post), secret: env.LINKEDIN_ACCESS_TOKEN,
  };
}

function facebook() {
  const graph = `https://graph.facebook.com/${env.FB_GRAPH_VERSION || 'v26.0'}/${env.FB_PAGE_ID || '<FB_PAGE_ID>'}`;
  if (image) {
    // A photo post: the picture with the text (and link) as its caption.
    const form = new FormData();
    form.set('source', new Blob([imageBytes()], { type: image.type }), image.path.split('/').pop());
    form.set('caption', withLink());
    if (image.alt) form.set('alt_text_custom', image.alt);
    form.set('access_token', env.FB_PAGE_TOKEN || '');
    const fields = { source: `<${image.path}, ${statSync(join(ROOT, image.path)).size} bytes>`,
      caption: withLink(), alt_text_custom: image.alt, access_token: env.FB_PAGE_TOKEN || '' };
    return { method: 'POST', url: `${graph}/photos`, headers: { 'Content-Type': 'multipart/form-data' },
      body: form, shown: JSON.stringify(fields, null, 2), secret: env.FB_PAGE_TOKEN };
  }
  const form = new URLSearchParams({ message: body, access_token: env.FB_PAGE_TOKEN || '' });
  if (meta.link) form.set('link', meta.link);
  return {
    method: 'POST', url: `${graph}/feed`,
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: form.toString(), secret: env.FB_PAGE_TOKEN,
  };
}

function youtubeInit(token) {
  const video = join(ROOT, meta.video);
  return {
    method: 'POST',
    url: 'https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status',
    headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json; charset=UTF-8',
      'X-Upload-Content-Type': 'video/mp4', 'X-Upload-Content-Length': String(statSync(video).size) },
    body: JSON.stringify({
      snippet: { title: meta.title, description: body, categoryId: '27',
        tags: (meta.tags || '').split(',').map((t) => t.trim()).filter(Boolean) },
      status: { privacyStatus: 'private', selfDeclaredMadeForKids: false },
    }),
    secret: token,
  };
}

function show(req) {
  const hide = (s) => (req.secret ? String(s).split(req.secret).join(mask(req.secret)) : s);
  const headers = Object.fromEntries(Object.entries(req.headers).map(([k, v]) => [k, hide(v)]));
  console.log(`${req.method} ${hide(req.url)}`);
  console.log(JSON.stringify(headers, null, 2));
  console.log(hide(req.shown ?? req.body));
}

async function send(req) {
  // fetch writes its own multipart Content-Type (with the boundary) for a form.
  const headers = { ...req.headers };
  if (req.body instanceof FormData) delete headers['Content-Type'];
  const res = await fetch(req.url, { method: req.method, headers, body: req.body });
  if (!res.ok) throw new Error(`${res.status} ${res.statusText}: ${(await res.text()).slice(0, 400)}`);
  return res;
}

// LinkedIn with an image: register it, upload it, then post with it.
async function linkedinWithImage() {
  const init = linkedinImageInit();
  console.log('Step 1 of 3 — register the image');
  show(init);
  let uploadUrl = '<uploadUrl-from-step-1>';
  let imageUrn = '<image-urn-from-step-1>';
  if (live) ({ uploadUrl, image: imageUrn } = (await (await send(init)).json()).value);
  const up = linkedinImageUpload(uploadUrl);
  console.log('\nStep 2 of 3 — upload the image');
  show(up);
  if (live) await send(up);
  console.log('\nStep 3 of 3 — post with the image');
  return linkedin(imageUrn);
}

async function main() {
  console.log(`${live ? 'LIVE' : 'DRY RUN'} · ${id} · ${meta.channel} · ${row.file}\n`);
  if (meta.channel === 'newsletter') {
    console.log('Newsletters are not posted by this script — they go out from your email tool as drafts (Lab 11).');
    return;
  }
  if (meta.channel === 'linkedin' || meta.channel === 'facebook') {
    const token = meta.channel === 'linkedin' ? env.LINKEDIN_ACCESS_TOKEN : env.FB_PAGE_TOKEN;
    if (live && !token) throw new Error(`no ${meta.channel} token in .env — see data/connect-accounts.md`);
    const req = meta.channel === 'facebook' ? facebook() : image ? await linkedinWithImage() : linkedin();
    show(req);
    if (!live) return console.log(`\nDry run — nothing was sent.${image ? ` Image: ${image.path}` : ''}`);
    const res = await send(req);
    // A Facebook photo post returns post_id (the feed post); a text post returns id.
    const postId = meta.channel === 'linkedin' ? res.headers.get('x-restli-id')
      : await res.json().then((j) => j.post_id || j.id);
    const url = meta.channel === 'linkedin' ? `https://www.linkedin.com/feed/update/${postId}/` : `https://www.facebook.com/${postId}`;
    logPublish(id, meta.channel, postId, url);
    return console.log(`\nPosted: ${url}`);
  }
  if (meta.channel === 'youtube') {
    let token = '<access-token-from-refresh-token>';
    if (live) {
      if (!env.YOUTUBE_REFRESH_TOKEN) throw new Error('no YOUTUBE_REFRESH_TOKEN in .env — see data/connect-accounts.md');
      const t = await send({ method: 'POST', url: 'https://oauth2.googleapis.com/token',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({ client_id: env.YOUTUBE_CLIENT_ID, client_secret: env.YOUTUBE_CLIENT_SECRET,
          refresh_token: env.YOUTUBE_REFRESH_TOKEN, grant_type: 'refresh_token' }).toString() });
      token = (await t.json()).access_token;
    }
    const init = youtubeInit(token);
    show(init);
    console.log(`\nthen: PUT <upload-url> with ${meta.video} (${statSync(join(ROOT, meta.video)).size} bytes)`);
    if (!live) return console.log('\nDry run — nothing was uploaded.');
    const where = (await send(init)).headers.get('location');
    const up = await send({ method: 'PUT', url: where, headers: { 'Content-Type': 'video/mp4' },
      body: readFileSync(join(ROOT, meta.video)) });
    const videoId = (await up.json()).id;
    logPublish(id, 'youtube', videoId, `https://studio.youtube.com/video/${videoId}/edit`);
    return console.log(`\nUploaded as PRIVATE: https://studio.youtube.com/video/${videoId}/edit`);
  }
  throw new Error(`unknown channel "${meta.channel}"`);
}

main().catch((e) => { console.error(`FAILED: ${e.message}`); process.exit(1); });
