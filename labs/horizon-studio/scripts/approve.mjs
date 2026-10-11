// node scripts/approve.mjs <id> --by "Your Name" [--changes "what to fix"]
// PEOPLE ONLY. Approves the CURRENT version of an item (records name, time
// and hash) or sends it back. Refuses to run without an interactive
// terminal, so an agent's tool call cannot approve anything.
import { existsSync } from 'node:fs';
import { join } from 'node:path';
import { ROOT, readRows, writeRows, hashOf } from './lib.mjs';

if (!process.stdin.isTTY || !process.stdout.isTTY) {
  console.error(existsSync(join(ROOT, 'scripts', 'approve-chat.mjs'))
    ? 'Only a person can approve. Ask them to type in the chat: approved <id> by <their name> — never ask them to run a command.'
    : 'approve.mjs must be run by a person in their own terminal — not by an agent.');
  process.exit(2);
}
const [id, ...rest] = process.argv.slice(2);
const opt = (k) => (rest.includes(k) ? rest[rest.indexOf(k) + 1] : '');
const by = opt('--by');
const changes = opt('--changes');
if (!id || !by) { console.error('usage: node scripts/approve.mjs <id> --by "Your Name" [--changes "why"]'); process.exit(1); }

const rows = readRows();
const row = rows.find((r) => r.id === id);
if (!row) { console.error(`${id} is not in review/approvals.csv`); process.exit(1); }

row.sha256 = hashOf(row.file);          // the version the person just read
row.approver = by;
row.approved_at = new Date().toISOString();
row.status = changes ? 'changes' : 'approved';
row.notes = changes;
writeRows(rows);
console.log(changes ? `${id} sent back: ${changes}` : `${id} approved by ${by} (sha256 ${row.sha256.slice(0, 12)}…)`);
