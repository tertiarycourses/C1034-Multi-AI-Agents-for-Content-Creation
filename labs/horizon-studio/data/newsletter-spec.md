# Newsletter build spec (Lab 11)

Output folder: content/newsletter/2026-11/
- issue.md — the approved text (frontmatter: id nl-2026-11, channel
  newsletter, subject, preview).
- newsletter.html — 600px wide, inline CSS only, brand colours, real text
  (not an image), alt text on every image, a visible "View in browser"
  link placeholder, unsubscribe link, the firm's address and the short
  disclaimer.
- newsletter.txt — the plain-text version.
- recipients.csv — only consent = yes AND unsubscribed = no.
- excluded.csv — everyone else, with the reason.
Build it ONLY from the version a person approved (check review/approvals.csv
and the hash). Gmail: create one DRAFT per recipient, or one draft to
yourself to test. Never send.
