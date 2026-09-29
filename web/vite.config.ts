import { defineConfig, type Plugin } from 'vite';
import react from '@vitejs/plugin-react';
import fs from 'node:fs';
import path from 'node:path';

const repoRoot = path.resolve(__dirname, '..');

// Serves images/PDFs referenced with relative paths from the repo's Markdown files,
// e.g. "MATH 4511/assignment1_images/page01.jpg" -> /repo/MATH%204511/assignment1_images/page01.jpg
const allowedExt = new Set(['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.pdf']);
const mime: Record<string, string> = {
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.webp': 'image/webp',
  '.pdf': 'application/pdf',
};

function repoAssets(): Plugin {
  return {
    name: 'repo-assets',
    configureServer(server) {
      server.middlewares.use('/repo', (req, res, next) => {
        const rel = decodeURIComponent((req.url ?? '').split('?')[0]);
        const abs = path.normalize(path.join(repoRoot, rel));
        const ext = path.extname(abs).toLowerCase();
        if (!abs.startsWith(repoRoot) || abs.includes(`${path.sep}.git${path.sep}`) || !allowedExt.has(ext)) {
          return next();
        }
        fs.stat(abs, (err, st) => {
          if (err || !st.isFile()) return next();
          res.setHeader('Content-Type', mime[ext] ?? 'application/octet-stream');
          fs.createReadStream(abs).pipe(res);
        });
      });
    },
  };
}

export default defineConfig({
  plugins: [react(), repoAssets()],
  server: {
    port: 8010,
    open: !process.env.NO_OPEN, // NO_OPEN=1 npm run dev  -> start without launching a browser
    fs: { allow: [repoRoot] },
  },
});
