// node scripts/serve-site.mjs [port]
// Serves YOUR copy of Horizon's website (web/site/) at http://localhost:8080
// so posts can link to it. Runs until stopped. Node 22, no packages.
// If the port is already in use, the site is most likely running already.
import { createServer } from 'node:http';
import { existsSync, readFileSync, statSync } from 'node:fs';
import { extname, join, normalize, resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const SITE = resolve(dirname(fileURLToPath(import.meta.url)), '..', 'web', 'site');
const PORT = Number(process.argv[2] || process.env.PORT || 8080);
const TYPES = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript',
  '.json': 'application/json', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg',
  '.gif': 'image/gif', '.svg': 'image/svg+xml', '.pdf': 'application/pdf', '.ico': 'image/x-icon',
  '.webp': 'image/webp', '.txt': 'text/plain; charset=utf-8' };

const server = createServer((req, res) => {
  // Drop the query string (UTM tags) and keep every path inside web/site/.
  const path = decodeURIComponent(new URL(req.url, 'http://localhost').pathname);
  let file = normalize(join(SITE, path));
  if (!file.startsWith(SITE)) { res.writeHead(403).end('Forbidden'); return; }
  if (existsSync(file) && statSync(file).isDirectory()) file = join(file, 'index.html');
  if (!existsSync(file)) { res.writeHead(404, { 'Content-Type': 'text/plain' }).end('Page not found'); return; }
  res.writeHead(200, { 'Content-Type': TYPES[extname(file).toLowerCase()] || 'application/octet-stream' });
  res.end(readFileSync(file));
});

server.on('error', (e) => {
  if (e.code === 'EADDRINUSE') {
    console.log(`Port ${PORT} is in use — your site is probably already running at http://localhost:${PORT}/`);
    process.exit(0);
  }
  throw e;
});
server.listen(PORT, '127.0.0.1', () =>
  console.log(`Your Horizon website is running at http://localhost:${PORT}/ (stop with Ctrl+C)`));
