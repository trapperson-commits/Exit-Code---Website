import { readFile, writeFile, mkdir, copyFile, stat, rm } from 'node:fs/promises';
import path from 'node:path';

const root = process.cwd();
const output = path.join(root, 'dist');
if (path.dirname(output) !== root || path.basename(output) !== 'dist') throw new Error('Invalid output directory');
let html = await readFile(path.join(root, 'koncepcio-3-szabad-ter.html'), 'utf8');
html = html.replace(/<a class="preview"[^>]*>.*?<\/a>/s, '');
// All layout and interactions are already implemented in the inline CSS/JS.
html = html.replace(/<script src="https:\/\/cdn\.tailwindcss\.com"><\/script>/g, '');
html = html.replace('<title>Exit Code — A way forward</title>', '<title>Exit Code | Nu metal from Berlin</title>');
// This generated directory must contain only the current release assets.
await rm(output, { recursive: true, force: true });
await mkdir(output, { recursive: true });
await writeFile(path.join(output, 'index.html'), html);

const copied = new Set();
const candidates = [...html.matchAll(/(?:src|href)="([^"]+)"|url\(["']?([^\)"']+)["']?\)/g)];
for (const match of candidates) {
  const reference = match[1] || match[2];
  if (/^(?:https?:|mailto:|data:|#)/.test(reference)) continue;
  const relative = decodeURIComponent(reference.split('#')[0].split('?')[0]);
  if (!relative || copied.has(relative)) continue;
  const source = path.resolve(root, relative);
  if (!source.startsWith(root + path.sep)) throw new Error(`Invalid asset path: ${relative}`);
  if (!(await stat(source)).isFile()) throw new Error(`Missing asset: ${relative}`);
  const target = path.join(output, relative);
  await mkdir(path.dirname(target), { recursive: true });
  await copyFile(source, target);
  copied.add(relative);
}
await writeFile(path.join(output, '404.html'), '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Page not found | Exit Code</title><body style="background:#181818;color:white;font:20px Arial;padding:10vw"><h1>Page not found</h1><a href="/" style="color:white">Back to Exit Code</a></body></html>');
console.log(`Production site prepared in dist/: index.html, 404.html and ${copied.size} assets.`);
