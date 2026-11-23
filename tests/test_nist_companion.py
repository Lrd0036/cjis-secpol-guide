"""Companion navigation/coverage structure checks, not normative validation.

Run with the repository suite: python -m unittest discover -s tests -v
No network requests; these checks cannot prove source accuracy or compliance.
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
GUIDE = 'docs/FROM-NIST-TO-CJIS.md'
APPENDIX = 'docs/CJIS-6.0-TO-6.1-CHANGES.md'
EXAMPLE = 'examples/NIST-TO-CJIS-INCIDENT-REPORTING.md'
MANIFEST = 'sources/manifests/nist-to-cjis-companion.md'
FILES = (GUIDE, APPENDIX, EXAMPLE, MANIFEST)
LINK = re.compile(r'\[[^\]\n]+\]\(([^)\s]+)\)')


def heading_ids(text: str) -> set[str]:
    """Subset of GitHub heading IDs used by these simple Markdown documents."""
    found = set()
    for line in text.splitlines():
        if re.match(r'^#{1,6} ', line):
            label = re.sub(r'^#+ ', '', line).strip().lower()
            label = re.sub(r'[^\w\- ]', '', label)
            found.add(label.replace(' ', '-'))
    return found


class NistCompanionTests(unittest.TestCase):
    def test_local_links_and_fragments(self) -> None:
        for relative in FILES:
            path = ROOT / relative
            for href in LINK.findall(path.read_text()):
                parsed = urlsplit(href)
                if parsed.scheme or parsed.netloc:
                    continue
                target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
                with self.subTest(source=relative, href=href):
                    self.assertTrue(target.is_relative_to(ROOT))
                    self.assertTrue(target.exists())
                    if parsed.fragment:
                        self.assertIn(unquote(parsed.fragment), heading_ids(target.read_text()))

    def test_readme_navigation_and_source_index(self) -> None:
        self.assertIn(f']({GUIDE})', (ROOT / 'README.md').read_text())
        self.assertIn('manifests/nist-to-cjis-companion.md',
                      (ROOT / 'sources/RESEARCH-NOTES.md').read_text())
        manifest = (ROOT / MANIFEST).read_text()
        for source_id in ('C61', 'C60', 'RC61', 'N53', 'N53B', 'N520'):
            self.assertRegex(manifest, rf'\| {source_id} \|')
        self.assertEqual(len(re.findall(r'`[0-9a-f]{64}`', manifest)), 6)

    def test_six_examples_have_distinct_evidence_and_caveats(self) -> None:
        text = (ROOT / GUIDE).read_text()
        sections = re.findall(r'### 4\.\d .*?(?=\n### |\n## |\Z)', text, re.S)
        self.assertEqual(len(sections), 6)
        for section in sections:
            self.assertIn('**NIST starting point.**', section)
            self.assertIn('**CJIS requirement summary.**', section)
            self.assertIn('**Suggested demonstration.**', section)
            self.assertIn('**Boundary and caveat.**', section)
        self.assertIn('not a complete crosswalk', text)
        self.assertIn('fictional', (ROOT / EXAMPLE).read_text().lower())
        self.assertIn('verified subset', (ROOT / APPENDIX).read_text())


if __name__ == '__main__':
    unittest.main()
