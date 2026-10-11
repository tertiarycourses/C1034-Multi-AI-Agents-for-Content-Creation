// node scripts/submit.mjs <content-file> [--by "agent name"]
// Adds (or refreshes) a PENDING row for the file's current version.
// Agents may run this: submitting is asking, not approving.
import { existsSync } from 'node:fs';
import { join } from 'node:path';
import { ROOT, readRows, writeRows, readContent, hashOf } from './lib.mjs';

const [file, ...rest] = process.argv.slice(2);
if (!file) { console.error('usage: node scripts/submit.mjs <content-file> [--by "name"]'); process.exit(1); }
const by = rest.includes('--by') ? rest[rest.indexOf('--by') + 1] : 'agent';

const { meta } = readContent(file);
if (!meta.id || !meta.channel) { console.error(`${file}: frontmatter needs id and channel`); process.exit(1); }

const rows = readRows();
const sha256 = hashOf(file);
const row = rows.find((r) => r.id === meta.id);
const fresh = { id: meta.id, channel: meta.channel, file, sha256, status: 'pending',
  submitted_by: by, approver: '', approved_at: '', notes: '' };
if (row) Object.assign(row, fresh); else rows.push(fresh);
writeRows(rows);
// Claude Code studios approve in the chat (approve-chat.mjs hook): never
// show a learner a command there.
const chat = existsSync(join(ROOT, 'scripts', 'approve-chat.mjs'));
console.log(`${meta.id} submitted for review (pending). ` + (chat
  ? `A person approves it by typing in the chat:\n  approved ${meta.id} by <their name>`
  : `A person approves it with:\n  node scripts/approve.mjs ${meta.id} --by "Your Name"`));
