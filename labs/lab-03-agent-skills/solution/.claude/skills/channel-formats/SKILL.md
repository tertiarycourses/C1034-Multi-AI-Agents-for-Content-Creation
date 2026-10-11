---
name: channel-formats
description: Use when writing a LinkedIn post, Facebook post, newsletter issue, YouTube script or page copy. The shape of each channel, UTM links, the short disclaimer and the content-file frontmatter.
---
# Channel formats
- LinkedIn: 120-250 words, a first line that stands alone, 3 hashtags.
- Facebook: 60-150 words, warm, ends with a question, an image idea + alt.
- Newsletter: subject < 50 chars, preview < 90, one tip, one nudge, one
  CTA; footer: unsubscribe, address, short disclaimer.
- YouTube: 60-90 s, 5-7 scenes (seconds, title, text); description with
  chapters, link, disclaimer, AI disclosure; 5-8 tags.
- Links go to our own website, http://localhost:8080/<page>, and carry
  ?utm_source=<channel>&utm_medium=<social|email|video>
  &utm_campaign=<campaign>. Never a private share link or the public
  site.
- One file per piece with the frontmatter in data/publishing-spec.md.
- Short disclaimer last: "General information only, not financial advice."
- Images: a PNG or JPG beside its post, named after the post id; fill in
  the post's image: and alt: lines. LinkedIn 1200 x 627, Facebook
  1080 x 1080; at most 8 words, disclaimer readable on a phone.
- A post and its image are approved together: a new image after approval
  needs a new approval.
- Going out: a person posts the approved text and image by hand, or
  scripts/publish.mjs posts both (dry run first, live only after a
  person says go). Never both for the same post.
