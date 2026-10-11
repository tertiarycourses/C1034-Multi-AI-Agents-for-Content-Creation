// UserPromptSubmit hook for Claude Code (.claude/settings.json).
// A person approves by TYPING in the chat — no terminal, no commands:
//   approved <id> by <your name>
//   changes <id>: what to fix
// This hook runs on the person's own message before Claude sees it, so an
// agent cannot approve anything: agents never write a user prompt, and the
// approval gate (gate-hook.mjs) stops them editing review/approvals.csv.
import { readRows, writeRows, hashOf } from './lib.mjs';

let raw = '';
for await (const chunk of process.stdin) raw += chunk;
let prompt = '';
try { prompt = String(JSON.parse(raw || '{}').prompt ?? ''); } catch { process.exit(0); }

const done = [];
const rows = (() => { try { return readRows(); } catch { return null; } })();
if (!rows) process.exit(0);

for (const line of prompt.split(/\r?\n/)) {
  const ok = line.match(/^\s*approved?\s+([\w.-]+(?:[\s,]+[\w.-]+)*?)(?:\s+by\s+(.+?))?\s*\.?\s*$/i);
  const back = line.match(/^\s*changes?\s+([\w.-]+)\s*:\s*(.+)$/i);
  const ids = ok ? ok[1].split(/[\s,]+/).filter(Boolean) : back ? [back[1]] : [];
  for (const id of ids) {
    const row = rows.find((r) => r.id === id);
    if (!row) { done.push(`${id}: not found in review/approvals.csv — nothing recorded.`); continue; }
    try { row.sha256 = hashOf(row.file); }  // the version the person just read
    catch (e) { done.push(`${id}: could not read ${row.file} — ${e.message}. Nothing recorded.`); continue; }
    row.approver = (ok && ok[2]) || 'the person in the chat';
    row.approved_at = new Date().toISOString();
    row.status = back ? 'changes' : 'approved';
    row.notes = back ? back[2] : '';
    done.push(back ? `${id}: sent back — ${back[2]}` : `${id}: APPROVED by ${row.approver} (sha256 ${row.sha256.slice(0, 12)}…)`);
  }
}
if (done.length) {
  writeRows(rows);
  console.log('Approval gate — recorded from the person\'s own message:\n' + done.join('\n'));
}
process.exit(0);
