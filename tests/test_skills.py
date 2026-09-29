"""Structural regression tests; no model execution or compliance determination.

Run: python -m unittest discover -s tests -p 'test_skills.py' -v
Only the deliberately simple, single-line frontmatter used by these two skills
is parsed here. This is not a general YAML or Agent Skills conformance library.
"""
from __future__ import annotations

import json
import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ('cjis-compliance-audit', 'is-this-cji')
VERDICTS = {
    'OUT_OF_SCOPE', 'FAIL', 'NOT_PROVEN', 'READY_FOR_AUTHORITY_REVIEW',
    'AUTHORITY_ACCEPTED', 'STALE',
}
DISPOSITIONS = {
    'CJI', 'CJI_DERIVED_PII', 'EXEMPT_TRANSACTION_IDENTIFIER',
    'AUTHORIZED_PUBLIC_INFORMATION', 'NOT_CJI', 'UNDETERMINED',
}
LINK = re.compile(r'\[[^\]\n]+\]\(([^)\s]+)\)')


def skill_file(name: str) -> Path:
    return ROOT / '.agents' / 'skills' / name / 'SKILL.md'


def read_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines()
    if not lines or lines[0] != '---':
        raise ValueError(f'{path}: missing opening frontmatter delimiter')
    try:
        end = lines.index('---', 1)
    except ValueError as exc:
        raise ValueError(f'{path}: missing closing frontmatter delimiter') from exc
    fields: dict[str, str] = {}
    for line in lines[1:end]:
        key, separator, value = line.partition(':')
        if not separator or not key or key in fields or not value.strip():
            raise ValueError(f'{path}: invalid or duplicate scalar field: {line!r}')
        fields[key] = value.strip()
    return fields, '\n'.join(lines[end + 1:])


class SkillStructureTests(unittest.TestCase):
    def test_exactly_two_discoverable_skills(self) -> None:
        found = {p.parent.name for p in (ROOT / '.agents/skills').glob('*/SKILL.md')}
        self.assertEqual(found, set(SKILLS))

    def test_frontmatter_and_size(self) -> None:
        for name in SKILLS:
            with self.subTest(skill=name):
                metadata, body = read_frontmatter(skill_file(name))
                self.assertEqual(set(metadata), {'name', 'description', 'license', 'compatibility'})
                self.assertEqual(metadata['name'], name)
                self.assertRegex(name, r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
                self.assertLessEqual(len(name), 64)
                self.assertTrue(1 <= len(metadata['description']) <= 1024)
                self.assertTrue(1 <= len(metadata['compatibility']) <= 500)
                self.assertEqual(metadata['license'], 'Apache-2.0')
                self.assertIn('checkout', metadata['compatibility'])
                self.assertLess(len(body.splitlines()), 500)
                self.assertIn('AGENT-SKILLS.md', body)

    def test_host_metadata(self) -> None:
        for name in SKILLS:
            with self.subTest(skill=name):
                text = (skill_file(name).parent / 'agents/openai.yaml').read_text(encoding='utf-8')
                self.assertTrue(text.startswith('interface:\n'))
                for key in ('display_name', 'short_description', 'default_prompt'):
                    self.assertRegex(text, rf'(?m)^  {key}: "[^"\n]+"$')
                self.assertIn(f'${name}', text)
                self.assertNotIn('dependencies:', text)

    def test_audit_contract(self) -> None:
        body = skill_file('cjis-compliance-audit').read_text(encoding='utf-8')
        for verdict in VERDICTS:
            self.assertIn(f'`{verdict}`', body)
        for template in ('SYSTEM-ASSESSMENT.md', 'CONTROL-EVIDENCE.md',
                         'VENDOR-QUESTIONNAIRE.md', 'AUTHORITY-DECISION.md'):
            self.assertIn(template, body)
        for term in ('enhancements', 'Operation', 'readiness', 'authority',
                     'NOT_APPLICABLE', 'INHERITED', 'support', 'sampling'):
            self.assertIn(term.lower(), body.lower())

    def test_classifier_contract(self) -> None:
        body = skill_file('is-this-cji').read_text(encoding='utf-8')
        template = (ROOT / 'templates/CJI-CLASSIFICATION.md').read_text(encoding='utf-8')
        for disposition in DISPOSITIONS:
            self.assertIn(f'`{disposition}`', body)
            self.assertIn(f'`{disposition}`', template)
        for term in ('Section 4.3', 'provenance', 'public', 'mixed', 'system', 'CHRI'):
            self.assertIn(term.lower(), body.lower())
        self.assertIn('../cjis-compliance-audit/SKILL.md', body)

    def test_all_local_markdown_links_resolve(self) -> None:
        paths = list((ROOT / '.agents/skills').rglob('*.md'))
        paths += [ROOT / 'docs/AGENT-SKILLS.md', ROOT / 'templates/CJI-CLASSIFICATION.md']
        for path in paths:
            for href in LINK.findall(path.read_text(encoding='utf-8')):
                parsed = urlsplit(href)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                target = (path.parent / unquote(parsed.path)).resolve()
                with self.subTest(source=str(path.relative_to(ROOT)), link=href):
                    self.assertTrue(target.is_relative_to(ROOT), 'link escapes repository')
                    self.assertTrue(target.exists(), f'missing target: {target}')

    def test_scenario_schema_and_coverage(self) -> None:
        fixture = json.loads((ROOT / 'tests/skill_cases.json').read_text(encoding='utf-8'))
        self.assertEqual(fixture['schema_version'], 1)
        self.assertIn('not recorded model runs', fixture['notice'])
        ids: set[str] = set()
        results: dict[str, set[str]] = {name: set() for name in SKILLS}
        for case in fixture['cases']:
            with self.subTest(case=case.get('id')):
                self.assertEqual(set(case), {'id', 'skill', 'prompt', 'expected_result',
                                             'must_include', 'must_not'})
                self.assertNotIn(case['id'], ids)
                ids.add(case['id'])
                self.assertIn(case['skill'], SKILLS)
                self.assertIsInstance(case['prompt'], str)
                self.assertTrue(case['prompt'].strip())
                for field in ('must_include', 'must_not'):
                    self.assertIsInstance(case[field], list)
                    self.assertTrue(case[field])
                    self.assertTrue(all(isinstance(s, str) and s.strip() for s in case[field]))
                allowed = VERDICTS if case['skill'] == 'cjis-compliance-audit' else DISPOSITIONS
                self.assertIn(case['expected_result'], allowed)
                results[case['skill']].add(case['expected_result'])
        self.assertEqual(results['cjis-compliance-audit'], VERDICTS)
        self.assertEqual(results['is-this-cji'], DISPOSITIONS)
        self.assertGreaterEqual(len(ids), 20)

    def test_handling_and_validation_limits_documented(self) -> None:
        doc = (ROOT / 'docs/AGENT-SKILLS.md').read_text(encoding='utf-8')
        for term in ('untrusted', 'public', 'sanitized', 'read-only',
                     'do **not** execute', 'complete repository', 'real path'):
            self.assertIn(term.lower(), doc.lower())
        self.assertIn('not output from a test that has already run', doc)


if __name__ == '__main__':
    unittest.main()
