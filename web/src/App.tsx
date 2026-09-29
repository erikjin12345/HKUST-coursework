import { useEffect, useMemo, useState } from 'react';
import MarkdownPage from './components/MarkdownPage';
import { pages, type Page } from './lib/pages';

function readHash(): string {
  return decodeURIComponent(window.location.hash.replace(/^#\/?/, ''));
}

export default function App() {
  const [current, setCurrent] = useState<string>(() => readHash());
  const [filter, setFilter] = useState('');

  useEffect(() => {
    const onHash = () => setCurrent(readHash());
    window.addEventListener('hashchange', onHash);
    return () => window.removeEventListener('hashchange', onHash);
  }, []);

  const page: Page | undefined = useMemo(
    () => pages.find((p) => p.id === current) ?? pages[0],
    [current],
  );

  useEffect(() => {
    if (page) document.title = `${page.title} – School Work`;
  }, [page]);

  const groups = useMemo(() => {
    const q = filter.trim().toLowerCase();
    const visible = q ? pages.filter((p) => `${p.group}/${p.title}`.toLowerCase().includes(q)) : pages;
    const m = new Map<string, Page[]>();
    for (const p of visible) m.set(p.group, [...(m.get(p.group) ?? []), p]);
    return [...m.entries()];
  }, [filter]);

  return (
    <div className="flex min-h-screen bg-white">
      <aside className="sticky top-0 h-screen w-72 shrink-0 overflow-y-auto border-r border-neutral-200 bg-neutral-50 p-4">
        <h1 className="mb-3 text-lg font-semibold">School Work</h1>
        <input
          type="search"
          value={filter}
          onChange={(e) => setFilter(e.target.value)}
          placeholder="Filtrera…"
          className="mb-4 w-full rounded border border-neutral-300 px-2 py-1 text-sm"
        />
        {groups.map(([group, items]) => (
          <section key={group} className="mb-4">
            <h2 className="mb-1 text-xs font-semibold uppercase tracking-wide text-neutral-500">{group}</h2>
            <ul>
              {items.map((p) => (
                <li key={p.id}>
                  <a
                    href={`#/${encodeURIComponent(p.id)}`}
                    className={`block rounded px-2 py-1 text-sm hover:bg-neutral-200 ${
                      page?.id === p.id ? 'bg-neutral-200 font-medium' : ''
                    }`}
                  >
                    {p.title}
                  </a>
                </li>
              ))}
            </ul>
          </section>
        ))}
        {pages.length === 0 && <p className="text-sm text-neutral-500">Inga sidor hittades.</p>}
      </aside>
      <main className="flex-1 px-10 py-8">
        {page ? (
          <>
            <p className="mb-2 font-mono text-xs text-neutral-500">{page.id}</p>
            <MarkdownPage page={page} />
          </>
        ) : (
          <p className="text-neutral-500">Lägg en .md-fil i web/content/ så visas den här.</p>
        )}
      </main>
    </div>
  );
}
