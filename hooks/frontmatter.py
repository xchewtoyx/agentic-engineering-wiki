"""Render OKF frontmatter for the docs site: description as a lede, sources as a footer."""

import html


def on_page_markdown(markdown, page, **kwargs):
    meta = page.meta
    description = meta.get("description")
    sources = meta.get("sources") or []
    if meta.get("type") != "concept":
        return markdown
    parts = []
    if description:
        parts.append(f'<p class="lede"><em>{html.escape(description.strip())}</em></p>\n')
    parts.append(markdown)
    if sources:
        items = "\n".join(
            f"- {s.get('resource') or s.get('title')}" for s in sources if isinstance(s, dict)
        )
        parts.append(f"\n\n---\n\n**Sources**\n\n{items}\n")
    return "".join(parts)
