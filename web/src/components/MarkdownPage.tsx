import { useEffect, useState } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import type { Page } from '../lib/pages';

type Props = { page: Page };

// Relative image/link paths in a repo Markdown file are resolved against the file's directory
// and served by the dev-server middleware under /repo/.
function makeUrlTransform(dir: string) {
  return (url: string) => {
    if (/^(https?:|mailto:|#|\/|data:)/i.test(url)) return url;
    const joined = dir ? `${dir}/${url}` : url;
    return `/repo/${joined.split('/').map(encodeURIComponent).join('/')}`;
  };
}

export default function MarkdownPage({ page }: Props) {
  const [source, setSource] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;
    setSource(null);
    setError(null);
    page
      .load()
      .then((s) => !cancelled && setSource(s))
      .catch((e: unknown) => !cancelled && setError(String(e)));
    return () => {
      cancelled = true;
    };
  }, [page]);

  if (error) return <p className="text-red-700">Kunde inte läsa sidan: {error}</p>;
  if (source === null) return <p className="text-neutral-500">Laddar…</p>;

  return (
    <article className="prose-doc">
      <ReactMarkdown
        remarkPlugins={[remarkGfm, remarkMath]}
        rehypePlugins={[[rehypeKatex, { strict: false, throwOnError: false }]]}
        urlTransform={makeUrlTransform(page.dir)}
      >
        {source}
      </ReactMarkdown>
    </article>
  );
}
