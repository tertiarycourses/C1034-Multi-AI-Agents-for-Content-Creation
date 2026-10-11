// PreToolUse hook for Claude Code (.claude/settings.json) or Codex
// (.codex/hooks.json). Reads the tool call as JSON on stdin; exit 2 blocks
// the call and shows the reason to the agent. It matches on the whole tool
// input, so it works whatever shape the shell tool's input takes.
import { existsSync } from 'node:fs';
import { join } from 'node:path';
import { ROOT, liveBlocker } from './lib.mjs';

let raw = '';
for await (const chunk of process.stdin) raw += chunk;
let call = {};
try { call = JSON.parse(raw || '{}'); } catch { /* not JSON: allow */ }
const input = JSON.stringify(call.tool_input ?? call.input ?? call.arguments ?? '');
const block = (why) => { console.error(`BLOCKED by the approval gate: ${why}`); process.exit(2); };

// Only people approve.
// Claude studios approve in the chat only: never point a learner to a terminal.
const chat = existsSync(join(ROOT, 'scripts', 'approve-chat.mjs'));
if (/approve\.mjs/.test(input)) block(chat
  ? 'only a person approves content — ask them to type "approved <id> by <name>" in the chat. Never ask them to run a command.'
  : 'only a person approves content — they run approve.mjs in their own terminal.');

// Live publishing needs an approved, unchanged item.
const m = input.match(/publish\.mjs\s+([\w.-]+)/);
if (m && /--live\b/.test(input)) {
  const why = liveBlocker(m[1]);
  if (why) block(why);
}

// Agents may not rewrite the approval records.
const path = String(call.tool_input?.file_path ?? call.tool_input?.path ?? '');
if (/review[\\/](approvals|publish-log)\.csv$/.test(path)) block('agents may not edit the approval records.');
process.exit(0);
