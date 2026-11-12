#!/usr/bin/env python3
"""Mechanical checks for a ship-second-brain vault.

Usage:
    python check_vault.py VAULT              # check, exit 1 on any FAIL
    python check_vault.py VAULT --snapshot   # also record hashes of new raw files

Checks:
  raw/       front matter has date, origin, url; files recorded in
             .raw-manifest.json are unchanged and not deleted
  notes      front matter has date, source, owner, confidence; confidence is
             seen | verified | opinion; every source path exists
  verified   has at least one '> ' quote, and every quote appears in a source
  links      notes in the vault root link to another existing note
             (links to today.md / gaps.md do not count); broken links fail
  inbox/     notes waiting for review are counted, not failed
  today.md   exists and is under 20 lines

The script never edits notes or raw files. It cannot judge whether a quote
supports the claim; that stays with the reader.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

CONFIDENCE = {"seen", "verified", "opinion"}
NOTE_FIELDS = ("date", "source", "owner", "confidence")
RAW_FIELDS = ("date", "origin", "url")
SPECIAL = {"today.md", "gaps.md", "README.md", "index.md"}
MANIFEST = ".raw-manifest.json"
LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")
MDLINK_RE = re.compile(r"\]\(([^)\s]+\.md)\)")

results = []  # (level, path, message)


def report(level, path, msg):
    results.append((level, str(path), msg))


def parse_front_matter(text):
    """Return (fields, body). Handles 'key: value' and simple '- item' lists."""
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    block, body = text[3:end], text[end + 4:]
    fields, key = {}, None
    for line in block.splitlines():
        if not line.strip():
            continue
        item = re.match(r"^\s*-\s+(.*)$", line)
        if item and key:
            if not isinstance(fields[key], list):
                fields[key] = [fields[key]] if fields[key] else []
            fields[key].append(item.group(1).strip().strip("'\""))
            continue
        kv = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if kv:
            key = kv.group(1)
            fields[key] = kv.group(2).strip().strip("'\"")
    return fields, body


def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_raw(vault, snapshot):
    raw_dir = vault / "raw"
    if not raw_dir.is_dir():
        report("WARN", raw_dir, "no raw/ folder: nothing has been ingested")
        return
    manifest_path = vault / MANIFEST
    manifest = {}
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for rel, digest in manifest.items():
        p = vault / rel
        if not p.exists():
            report("FAIL", rel, "raw file deleted (rule: never delete a raw file)")
        elif sha(p) != digest:
            report("FAIL", rel, "raw file changed since it was saved (save a new dated file instead)")
    new = {}
    for p in sorted(raw_dir.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(vault).as_posix()
        if p.suffix == ".md":
            fields, _ = parse_front_matter(p.read_text(encoding="utf-8", errors="replace"))
            missing = [f for f in RAW_FIELDS if not (fields or {}).get(f)]
            if missing:
                report("FAIL", rel, f"raw front matter missing: {', '.join(missing)}")
        if rel not in manifest:
            new[rel] = sha(p)
    if new:
        if snapshot:
            manifest.update(new)
            manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            report("PASS", MANIFEST, f"recorded {len(new)} new raw file(s)")
        else:
            report("WARN", MANIFEST, f"{len(new)} raw file(s) not yet recorded; run with --snapshot after intake")


def note_files(vault):
    for p in sorted(vault.rglob("*.md")):
        rel = p.relative_to(vault)
        if rel.parts[0] in ("raw",) or rel.parts[0].startswith("."):
            continue
        if len(rel.parts) == 1 and rel.name in SPECIAL:
            continue
        yield p


def check_notes(vault):
    names = {p.stem: p for p in note_files(vault)}
    inbox = 0
    for p in names.values():
        rel = p.relative_to(vault)
        in_inbox = rel.parts[0] == "inbox"
        inbox += in_inbox
        text = p.read_text(encoding="utf-8", errors="replace")
        fields, body = parse_front_matter(text)
        if fields is None:
            report("FAIL", rel, "no front matter (see references/note-format.md)")
            continue
        missing = [f for f in NOTE_FIELDS if not fields.get(f)]
        if missing:
            report("FAIL", rel, f"front matter missing: {', '.join(missing)}")
        conf = fields.get("confidence", "")
        if conf and conf not in CONFIDENCE:
            report("FAIL", rel, f"confidence '{conf}' is not seen | verified | opinion")

        sources = fields.get("source") or []
        if isinstance(sources, str):
            sources = [sources]
        source_texts = []
        for s in sources:
            if re.match(r"^https?://", s):
                report("WARN", rel, f"source is a URL, not a raw file: {s} (rule: raw goes in first)")
                continue
            sp = vault / s
            if not sp.exists():
                report("FAIL", rel, f"source not found: {s}")
            else:
                source_texts.append(norm(sp.read_text(encoding="utf-8", errors="replace")))

        if conf == "verified":
            quotes = [l[1:].strip() for l in body.splitlines() if l.startswith(">") and l[1:].strip()]
            if not quotes:
                report("FAIL", rel, "verified but has no '> ' quote to check: downgrade to seen or add the quote")
            elif source_texts:
                for q in quotes:
                    if not any(norm(q) in t for t in source_texts):
                        report("FAIL", rel, f"quote not in source, downgrade to seen: \"{q[:70]}\"")

        targets = set(LINK_RE.findall(body)) | {Path(m).stem for m in MDLINK_RE.findall(body)
                                                 if not m.startswith(("raw/", "../raw/", "http"))}
        targets = {t.strip() for t in targets}
        broken = sorted(t for t in targets if t not in names and t not in ("today", "gaps"))
        for t in broken:
            report("FAIL", rel, f"broken link: [[{t}]]")
        real = [t for t in targets if t in names and t != p.stem]
        if not real and not in_inbox:
            report("FAIL", rel, "orphan: links to no other note; link it or move it to inbox/")
    report("PASS", "notes", f"{len(names)} note(s) checked, {inbox} in inbox/")


def check_today(vault):
    t = vault / "today.md"
    if not t.exists():
        report("WARN", "today.md", "missing (Pass 5 not run yet)")
        return
    n = len([l for l in t.read_text(encoding="utf-8").splitlines()])
    if n >= 20:
        report("FAIL", "today.md", f"{n} lines; keep it under 20")
    else:
        report("PASS", "today.md", f"{n} lines")


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 1:
        print(__doc__)
        return 2
    vault = Path(args[0])
    if not vault.is_dir():
        print(f"FAIL {vault}: not a folder")
        return 2
    check_raw(vault, "--snapshot" in argv)
    check_notes(vault)
    check_today(vault)
    for level, path, msg in results:
        print(f"{level:4} {path}: {msg}")
    counts = {k: sum(1 for r in results if r[0] == k) for k in ("PASS", "WARN", "FAIL")}
    print(f"\n{counts['PASS']} PASS, {counts['WARN']} WARN, {counts['FAIL']} FAIL")
    return 1 if counts["FAIL"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
