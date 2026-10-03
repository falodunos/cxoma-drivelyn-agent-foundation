#!/usr/bin/env python3
"""Exercise foundation acceptance failures in disposable copies."""
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
ROOT = Path(__file__).resolve().parent.parent
class FoundationTests(unittest.TestCase):
    def test_rejects_workflow_template_and_version_drift(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d) / 'foundation'
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns('.git', '__pycache__'))
            command = [str(root / 'scripts/validate-foundation')]
            self.assertEqual(subprocess.run(command, capture_output=True).returncode, 0)
            version = root / 'VERSION'; original = version.read_text()
            version.write_text('9.9.9\n')
            self.assertNotEqual(subprocess.run(command,capture_output=True).returncode,0)
            version.write_text(original)
            role = root / 'reviewer-templates/learning-safety-reviewer.toml'
            role.write_text(role.read_text().replace('sandbox_mode = "read-only"','sandbox_mode = "workspace-write"'))
            self.assertNotEqual(subprocess.run(command,capture_output=True).returncode,0)
    def test_rejects_missing_workflow_policy(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d) / 'foundation'
            shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('.git','__pycache__'))
            (root / 'principles/autonomous-work-policy.md').unlink()
            self.assertNotEqual(subprocess.run([str(root / 'scripts/validate-foundation')],capture_output=True).returncode,0)
if __name__ == '__main__': unittest.main()
