#!/usr/bin/env python3
"""Self-check for check_pages.py: python -I tests/test_check_pages.py"""
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "skills" / "paper-trail" / "scripts" / "check_pages.py"

FACTS = """- legal_name*: Example Studio LLP
- product_name*: Tidy Notes
- product_url*: https://tidynotes.app
- contact_email*: hello@tidynotes.app
- processors*: Stripe (stripe.com) for payments; Plausible (plausible.io) for analytics
- retention*: [NEEDS: how long sign-up emails are kept]
"""

PRIVACY = """# Privacy policy

Last updated: 2026-10-24

## Who we are
Tidy Notes is run by Example Studio LLP.

## What we collect
Your email address when you sign up.

## Why we collect it
To send you your login link.

## Who we share it with
Stripe (https://stripe.com/privacy) processes payments. Plausible (https://plausible.io) counts visits.

## How long we keep it
Until you delete your account.

## Your rights
Email us to see, correct or delete your data.

## Contact
hello@tidynotes.app
"""


def run(tmp, files, *pages, extra=()):
    for name, text in files.items():
        (tmp / name).write_text(text, encoding="utf-8")
    return subprocess.run([sys.executable, "-I", str(SCRIPT), "--facts", str(tmp / "facts.md"), *extra,
                           *[str(tmp / p) for p in pages]], capture_output=True, text=True)


with tempfile.TemporaryDirectory() as t:
    tmp = Path(t)
    # A clean page passes; the fact sheet's open [NEEDS] is only a warning.
    p = run(tmp, {"facts.md": FACTS, "privacy.md": PRIVACY}, "privacy.md")
    assert p.returncode == 0, p.stdout
    assert "PASS  " in p.stdout and "WARN  facts: retention" in p.stdout, p.stdout

    # An invented email, a placeholder, a missing section and a missing date each fail.
    bad = (PRIVACY.replace("hello@tidynotes.app", "privacy@tidynotes.app")
           .replace("Until you delete your account.", "[NEEDS: retention]")
           .replace("## Your rights", "## Misc").replace("Last updated: 2026-10-24", ""))
    p = run(tmp, {"facts.md": FACTS, "privacy.md": bad}, "privacy.md")
    assert p.returncode == 1, p.stdout
    for needle in ("privacy@tidynotes.app is not in the fact sheet", "placeholder '[NEEDS: retention]'",
                   "missing section: 'your rights'", "no 'Last updated"):
        assert needle in p.stdout, (needle, p.stdout)

    # An unknown link host warns but does not fail.
    p = run(tmp, {"facts.md": FACTS, "privacy.md": PRIVACY.replace("https://plausible.io", "https://fonts.googleapis.com")},
            "privacy.md")
    assert p.returncode == 0 and "fonts.googleapis.com is not in the fact sheet" in p.stdout, p.stdout

    # Terms: kind from the file name, required sections enforced.
    terms = "# Terms\n\nLast updated: 2026-10-01\n\n## The service\nNotes.\n\n## Contact\nhello@tidynotes.app\n"
    p = run(tmp, {"facts.md": FACTS, "privacy.md": PRIVACY, "terms-of-service.md": terms},
            "privacy.md", "terms-of-service.md")
    assert p.returncode == 1 and "(terms): missing section: 'acceptable use'" in p.stdout, p.stdout
    assert "different 'Last updated' dates" in p.stdout, p.stdout

    # An unrecognised name needs --kind.
    p = run(tmp, {"facts.md": FACTS, "legal.md": PRIVACY}, "legal.md")
    assert p.returncode == 1 and "pass --kind" in p.stdout, p.stdout
    p = run(tmp, {"facts.md": FACTS, "legal.md": PRIVACY}, "legal.md", extra=("--kind", "privacy"))
    assert p.returncode == 0, p.stdout

print("check_pages: ok")
