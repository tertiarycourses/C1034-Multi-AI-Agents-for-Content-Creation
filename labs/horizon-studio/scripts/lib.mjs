// Shared helpers for the Horizon publishing gate (Lab 10). Node 22, no packages.
import { createHash } from 'node:crypto';
import { existsSync, readFileSync, writeFileSync, appendFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

export const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
export const APPROVALS = join(ROOT, 'review', 'approvals.csv');
export const PUBLISH_LOG = join(ROOT, 'review', 'publish-log.csv');
const HEAD = 'id,channel,file,sha256,status,submitted_by,approver,approved_at,notes';

// --- CSV (quoted fields allowed) ------------------------------------------
function parseLine(line) {
  const out = []; let cur = ''; let q = false;
  for (let i = 0; i < line.length; i++) {
    const c = line[i];
    if (q) {
      if (c === '"' && line[i + 1] === '"') { cur += '"'; i++; }
      else if (c === '"') q = false;
      else cur += c;
    } else if (c === '"') q = true;
    else if (c === ',') { out.push(cur); cur = ''; }
    else cur += c;
  }
  out.push(cur);
  return out;
}
const quote = (v) => (/[",\n]/.test(v) ? `"${String(v).replace(/"/g, '""')}"` : String(v ?? ''));

export function readRows() {
  if (!existsSync(APPROVALS)) return [];
  const [head, ...lines] = readFileSync(APPROVALS, 'utf8').split(/\r?\n/).filter(Boolean);
  const keys = parseLine(head);
  return lines.map((l) => Object.fromEntries(parseLine(l).map((v, i) => [keys[i], v])));
}

export function writeRows(rows) {
  const keys = HEAD.split(',');
  const body = rows.map((r) => keys.map((k) => quote(r[k] ?? '')).join(','));
  writeFileSync(APPROVALS, [HEAD, ...body].join('\n') + '\n');
}

// --- content files ----------------------------------------------------------
export function readContent(file) {
  const text = readFileSync(join(ROOT, file), 'utf8');
  const m = text.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/);
  if (!m) throw new Error(`${file}: missing --- frontmatter ---`);
  const meta = {};
  for (const line of m[1].split(/\r?\n/)) {
    const kv = line.match(/^([A-Za-z_]+):\s*(.*?)\s*(#.*)?$/);
    if (kv) meta[kv[1]] = kv[2].replace(/^["']|["']$/g, '');
  }
  return { meta, body: m[2].trim() };
}

// The approved version = the content file, plus its image (social) or video
// (YouTube) — so swapping the picture after approval needs a new approval.
export function hashOf(file) {
  const h = createHash('sha256').update(readFileSync(join(ROOT, file)));
  const { meta } = readContent(file);
  const media = meta.channel === 'youtube' ? meta.video
    : ['linkedin', 'facebook'].includes(meta.channel) ? meta.image : '';
  if (media) {
    const m = join(ROOT, media);
    if (!existsSync(m)) throw new Error(`${meta.channel === 'youtube' ? 'video' : 'image'} not found: ${media}`);
    h.update(readFileSync(m));
  }
  return h.digest('hex');
}

// PNG, JPG or GIF only (LinkedIn's and Facebook's photo formats).
export function imageType(path) {
  const ext = path.toLowerCase().split('.').pop();
  const type = { png: 'image/png', jpg: 'image/jpeg', jpeg: 'image/jpeg', gif: 'image/gif' }[ext];
  if (!type) throw new Error(`image must be .png, .jpg or .gif: ${path}`);
  return type;
}

// Why an id may NOT go live, or null when it may.
export function liveBlocker(id) {
  const row = readRows().find((r) => r.id === id);
  if (!row) return `${id} is not in review/approvals.csv — run submit.mjs first.`;
  if (row.status !== 'approved') return `${id} is "${row.status}", not approved by a person.`;
  if (!row.approver || !row.approved_at) return `${id} has no approver name and date.`;
  if (hashOf(row.file) !== row.sha256) return `${id} changed after it was approved — a person must approve this version.`;
  if (publishedIds().has(id)) return `${id} was already published (review/publish-log.csv) — no double posts.`;
  return null;
}

export function publishedIds() {
  if (!existsSync(PUBLISH_LOG)) return new Set();
  return new Set(readFileSync(PUBLISH_LOG, 'utf8').split(/\r?\n/).slice(1)
    .filter(Boolean).map((l) => parseLine(l)[0]));
}

export function logPublish(id, channel, remoteId, url) {
  if (!existsSync(PUBLISH_LOG)) writeFileSync(PUBLISH_LOG, 'id,channel,published_at,remote_id,url\n');
  appendFileSync(PUBLISH_LOG, [id, channel, new Date().toISOString(), remoteId, url].map(quote).join(',') + '\n');
}

// --- .env (never printed) ---------------------------------------------------
export function loadEnv() {
  const env = { ...process.env };
  const f = join(ROOT, '.env');
  if (existsSync(f)) {
    for (const line of readFileSync(f, 'utf8').split(/\r?\n/)) {
      const m = line.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*)\s*$/);
      if (m && !line.trim().startsWith('#')) env[m[1]] = m[2].replace(/^["']|["']$/g, '');
    }
  }
  return env;
}

export const mask = (s) => (s ? `${String(s).slice(0, 4)}…(${String(s).length} chars)` : '(missing)');
