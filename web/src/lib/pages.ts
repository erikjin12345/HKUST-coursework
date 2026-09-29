// Discovers Markdown pages from two places:
//   1. web/content/**/*.md   – scratch pages written for the browser (derivations, explanations)
//   2. <repo>/**/*.md        – the courses' own files (CHEATSHEET.md, Assignment1.md, ...)
// The course submodule and tooling folders are excluded.

export type Page = {
  id: string;        // URL-safe key used in the hash, e.g. "MATH 4511/CHEATSHEET.md"
  title: string;     // Sidebar label
  group: string;     // Sidebar section, e.g. "MATH 4511" or "Scratch"
  dir: string;       // Directory relative to the repo root; used to resolve relative image paths
  load: () => Promise<string>;
};

// Paths are relative to this file (web/src/lib/): ../../ is web/, ../../../ is the repo root.
const scratch = import.meta.glob('../../content/**/*.md', { query: '?raw', import: 'default' }) as Record<
  string,
  () => Promise<string>
>;

const repo = import.meta.glob(
  [
    '../../../*/**/*.md',
    '../../../*.md',
    '!../../../web/**',
    '!../../../.venv/**',
    '!../../../**/node_modules/**',
    '!../../../**/MATH-4432-Statistical-Machine-Learning/**',
  ],
  { query: '?raw', import: 'default' },
) as Record<string, () => Promise<string>>;

function titleFromPath(p: string): string {
  const base = p.split('/').pop() ?? p;
  return base.replace(/\.md$/, '');
}

function build(): Page[] {
  const pages: Page[] = [];

  for (const [key, load] of Object.entries(scratch)) {
    const rel = key.replace(/^\.\.\/\.\.\/content\//, '');
    pages.push({ id: `scratch/${rel}`, title: titleFromPath(rel), group: 'Scratch', dir: 'web/content', load });
  }

  for (const [key, load] of Object.entries(repo)) {
    const rel = key.replace(/^(\.\.\/){3}/, '');
    const parts = rel.split('/');
    const group = parts.length > 1 ? parts[0] : 'Repo';
    const dir = parts.slice(0, -1).join('/');
    pages.push({ id: rel, title: titleFromPath(rel), group, dir, load });
  }

  const order = (g: string) => (g === 'Scratch' ? 0 : g === 'Repo' ? 1 : 2);
  return pages.sort((a, b) => order(a.group) - order(b.group) || a.group.localeCompare(b.group) || a.title.localeCompare(b.title));
}

export const pages: Page[] = build();
