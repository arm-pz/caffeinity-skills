#!/usr/bin/env node
// Replay a site prompt: materialize its `## File:` sections, or check them
// against an existing build. Zero dependencies.
//
//   node replay-prompt.mjs <prompt.md> --list
//   node replay-prompt.mjs <prompt.md> --out <fresh-dir>
//   node replay-prompt.mjs <prompt.md> --check <built-dir>

import fs from "node:fs";
import path from "node:path";

const USAGE = `Usage:
  node replay-prompt.mjs <prompt.md> --list
  node replay-prompt.mjs <prompt.md> --out <fresh-dir>
  node replay-prompt.mjs <prompt.md> --check <built-dir>`;

const IGNORED_DIRS = new Set(["node_modules", "dist", ".git", ".vite"]);
const IGNORED_FILES = new Set(["package-lock.json", "pnpm-lock.yaml", "yarn.lock", "npm-debug.log"]);
const BINARY_ASSETS = new Set([".png", ".jpg", ".jpeg", ".webp", ".avif", ".gif", ".ico", ".woff", ".woff2", ".ttf", ".otf", ".mp4", ".webm", ".mp3", ".wav", ".ogg", ".pdf"]);

function fail(message) {
  console.error(`ERROR  ${message}`);
  process.exit(2);
}

function parseArgs(argv) {
  if (argv.length < 2) fail(USAGE);
  const promptPath = path.resolve(argv[0]);
  const mode = argv[1];
  const target = argv[2] ? path.resolve(argv[2]) : null;
  if (!["--list", "--out", "--check"].includes(mode)) fail(`unknown mode ${mode}\n${USAGE}`);
  if (mode !== "--list" && !target) fail(`${mode} needs a directory\n${USAGE}`);
  if (argv.length > 3) fail(`unexpected extra argument ${argv[3]}`);
  return { promptPath, mode, target };
}

function parseSections(text) {
  const lines = text.replace(/\r\n/g, "\n").split("\n");
  const sections = [];
  const seen = new Map();
  let i = 0;

  while (i < lines.length) {
    const stray = openFence(lines[i]);
    if (stray) {
      const close = findClose(lines, i, stray);
      if (close === -1) fail(`unclosed code fence at line ${i + 1}`);
      i = close + 1;
      continue;
    }

    const heading = lines[i].match(/^## File: `([^`]+)`[ \t]*$/);
    if (!heading) {
      i++;
      continue;
    }

    const rel = heading[1].trim();
    const problem = pathProblem(rel);
    if (problem) fail(`file section "${rel}": ${problem}`);
    const key = rel.toLowerCase();
    if (seen.has(key)) fail(`duplicate file section "${rel}" (also line ${seen.get(key)})`);
    seen.set(key, i + 1);

    let j = i + 1;
    while (j < lines.length && lines[j].trim() === "") j++;
    const open = j < lines.length ? openFence(lines[j]) : null;
    if (!open) fail(`file section "${rel}": expected a fenced code block right after the heading`);

    const content = [];
    let k = j + 1;
    let closed = false;
    while (k < lines.length) {
      if (isClose(lines[k], open)) {
        closed = true;
        break;
      }
      content.push(lines[k]);
      k++;
    }
    if (!closed) fail(`file section "${rel}": unclosed code fence`);

    let after = k + 1;
    while (after < lines.length && lines[after].trim() === "") after++;
    if (after < lines.length && !/^## /.test(lines[after])) {
      fail(`file section "${rel}": more than one code block (or text) after the first one`);
    }

    sections.push({ rel, content: content.length ? content.join("\n") + "\n" : "" });
    i = after;
  }

  if (!sections.length) fail("no `## File: `path`` headings found");
  return sections;
}

function openFence(line) {
  const match = line.match(/^ {0,3}(`{3,}|~{3,})(.*)$/);
  return match ? { marker: match[1][0], size: match[1].length } : null;
}

function isClose(line, open) {
  const match = line.match(/^ {0,3}(`{3,}|~{3,})[ \t]*$/);
  return Boolean(match && match[1][0] === open.marker && match[1].length >= open.size);
}

function findClose(lines, start, open) {
  for (let i = start + 1; i < lines.length; i++) {
    if (isClose(lines[i], open)) return i;
  }
  return -1;
}

function pathProblem(rel) {
  if (!rel) return "empty path";
  if (rel.includes("\\")) return "use forward slashes";
  if (rel.startsWith("/") || /^[a-zA-Z]:/.test(rel)) return "absolute path";
  const parts = rel.split("/");
  if (parts.some((p) => p === "" || p === "." || p === "..")) return "path must be relative and normalized";
  if (IGNORED_DIRS.has(parts[0]) && parts.length > 1) return `refusing to write into ${parts[0]}/`;
  if (parts.some((p) => IGNORED_DIRS.has(p) && p !== parts[parts.length - 1])) return "refusing to write inside an ignored directory";
  return null;
}

function extractFence(body) {
  const lines = body.split("\n");
  let i = 0;
  while (i < lines.length && lines[i].trim() === "") i++;
  if (i >= lines.length) return { error: "section has no fenced code block" };

  const open = lines[i].match(/^ {0,3}(`{3,}|~{3,})(.*)$/);
  if (!open) return { error: "expected a fenced code block right after the heading" };
  const marker = open[1][0];
  const size = open[1].length;

  const content = [];
  for (let j = i + 1; j < lines.length; j++) {
    const close = lines[j].match(/^ {0,3}(`{3,}|~{3,})[ \t]*$/);
    if (close && close[1][0] === marker && close[1].length >= size) {
      const trailing = lines.slice(j + 1).filter((l) => l.trim() !== "");
      if (trailing.length) return { error: "more than one code block (or text) after the first one" };
      return { content: content.length ? content.join("\n") + "\n" : "" };
    }
    content.push(lines[j]);
  }
  return { error: "unclosed code fence" };
}

function materialize(sections, target) {
  if (fs.existsSync(target)) {
    if (!fs.statSync(target).isDirectory()) fail(`${target} exists and is not a directory`);
    if (fs.readdirSync(target).length) fail(`${target} is not empty; pass a fresh directory`);
  }

  let bytes = 0;
  for (const section of sections) {
    const dest = path.resolve(target, section.rel);
    const relative = path.relative(target, dest);
    if (relative.startsWith("..") || path.isAbsolute(relative)) fail(`refusing to write outside target: ${section.rel}`);
    fs.mkdirSync(path.dirname(dest), { recursive: true });
    fs.writeFileSync(dest, section.content);
    bytes += Buffer.byteLength(section.content);
  }
  console.log(`Wrote ${sections.length} files (${bytes} bytes) to ${target}`);
}

function normalize(buffer) {
  return buffer.toString("utf8").replace(/\r\n/g, "\n");
}

function firstDifference(expected, actual) {
  const a = expected.split("\n");
  const b = actual.split("\n");
  const last = Math.max(a.length, b.length);
  for (let i = 0; i < last; i++) {
    if (a[i] !== b[i]) {
      return {
        line: i + 1,
        expected: a[i] === undefined ? "<end of file>" : JSON.stringify(a[i]).slice(0, 160),
        actual: b[i] === undefined ? "<end of file>" : JSON.stringify(b[i]).slice(0, 160),
      };
    }
  }
  return null;
}

function check(sections, dir) {
  if (!fs.existsSync(dir) || !fs.statSync(dir).isDirectory()) fail(`${dir} is not a directory`);

  let mismatches = 0;
  const missing = [];
  const drifted = [];

  for (const section of sections) {
    const file = path.join(dir, section.rel);
    if (!fs.existsSync(file) || !fs.statSync(file).isFile()) {
      missing.push(section.rel);
      continue;
    }
    const expected = normalize(Buffer.from(section.content));
    const actual = normalize(fs.readFileSync(file));
    if (expected !== actual) {
      mismatches++;
      const diff = firstDifference(expected, actual);
      drifted.push({ rel: section.rel, ...diff });
    }
  }

  const extras = listFiles(dir)
    .filter((rel) => !sections.some((s) => s.rel.toLowerCase() === rel.toLowerCase()));
  const assets = extras.filter((rel) => BINARY_ASSETS.has(path.extname(rel).toLowerCase()));
  const strayFiles = extras.filter((rel) => !assets.includes(rel));

  for (const rel of missing) console.log(`MISSING  ${rel}`);
  for (const d of drifted) {
    console.log(`DIFF     ${d.rel} (line ${d.line})`);
    console.log(`  prompt: ${d.expected}`);
    console.log(`  built:  ${d.actual}`);
  }
  for (const rel of strayFiles) console.log(`EXTRA    ${rel} (text file not in prompt)`);
  for (const rel of assets) console.log(`ASSET    ${rel} (binary, expected from the Assets section)`);

  const ok = missing.length === 0 && drifted.length === 0 && strayFiles.length === 0;
  console.log(`\n${sections.length} sections: ${sections.length - missing.length - drifted.length} match, ${drifted.length} differ, ${missing.length} missing; ${strayFiles.length} extra text, ${assets.length} binary assets`);
  if (!ok) process.exitCode = 1;
}

function listFiles(root) {
  const out = [];
  const walk = (dir, prefix) => {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const rel = prefix ? `${prefix}/${entry.name}` : entry.name;
      if (entry.isDirectory()) {
        if (IGNORED_DIRS.has(entry.name)) continue;
        walk(path.join(dir, entry.name), rel);
      } else if (!IGNORED_FILES.has(entry.name)) {
        out.push(rel);
      }
    }
  };
  walk(root, "");
  return out.sort();
}

const { promptPath, mode, target } = parseArgs(process.argv.slice(2));
const text = fs.readFileSync(promptPath, "utf8");
const sections = parseSections(text);

if (mode === "--list") {
  for (const section of sections) {
    const lines = section.content ? section.content.split("\n").length - 1 : 0;
    console.log(`${String(lines).padStart(5)}  ${section.rel}`);
  }
  console.log(`\n${sections.length} files, ${sections.reduce((n, s) => n + Buffer.byteLength(s.content), 0)} bytes`);
} else if (mode === "--out") {
  materialize(sections, target);
} else {
  check(sections, target);
}
