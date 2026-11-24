# Build Report — Two-Sentence Horror

Bounty: [u-suroto-two-sentence-horror-acea9253](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253)
Prize: $2, winner-takes-all · Free entry · Deadline: 27 Nov 2026 15:00 WIB

## Final story

> The previous owners had no children, yet the nursery was painted pale yellow and smelled faintly of milk. This morning I found my daughter's name written in the dust beneath the window; we haven't chosen one yet.

- **Characters: 212** (gate limit: 400)
- **Sentences: 2** (exactly, as required)
- **Bytes: 212** (pure ASCII, no trailing newline)

## Why this story

- The second sentence turns the first: a nursery prepared for a child the
  previous owners never had is already uncanny — then the name written in
  the dust belongs to a daughter whose name has not been chosen yet, so
  something else chose it first. On a second read, the painted room and the
  smell of milk stop being leftovers and become preparations.
- The horror is implied, never explained: nothing is named, nothing jumps
  out, and the reader fills in who wrote the name and what it wants.
- Concrete and restrained throughout (pale yellow, faint smell of milk,
  dust beneath the window); no gore, no familiar twist (no mirror, no
  phone call from inside, no "it was me all along").

## Local verification (24 Nov 2026)

Command:

```sh
OUTPUT_DIR=/tmp/horror-test-out python3 main.py
```

Result:

```text
OK: wrote /tmp/horror-test-out/entry.txt
characters: 212 (max 400)
sentences: 2
bytes: 212
read-back: byte-for-byte identical
```

Independent re-check of the written file: 212 bytes, 212 characters,
2 periods (2 sentences), no trailing newline, ASCII only. Program writes
atomically (temp file + `os.replace`) and verifies the read-back
byte-for-byte before reporting success; default output path is
`/output/entry.txt` (overridden here only via `OUTPUT_DIR` for the local
test).

## Revision (24 Nov 2026)

One real fix in `main.py`, no change to the story: `count_sentences`
was a bare `re.findall(r"[.!?](?:\s|$)", text)`, so it miscounted any
period that is not a sentence end — "Mr. Smith went home." counted as
2 sentences, "No. 5 arrived today." as 2, "The U.S. Army marched.
Then it stopped." as 3. The revised counter:

- collapses ellipsis runs (adjacent or space-separated dots) to one
  terminator, so "..." / ". . ." counts once;
- skips a period ending a known abbreviation (`mr`, `mrs`, `ms`, `dr`,
  `st`, `jr`, `sr`, `vs`, `etc`, `e.g`, `i.e`, `no`, `fig`, `approx`,
  `dept`);
- skips a period ending a single capital initial or a run of capital
  initials (`J.`, `U.S.`, `J. R. R.`).

Verified against 9 cases (all pass): `Mr. Smith went home.` → 1,
`Dr. No arrived. He stayed.` → 2, `Wait... Really?` → 2,
`No. 5 arrived today.` → 1, `The U.S. Army marched. Then it stopped.`
→ 2, `J. R. R. Tolkien wrote. He wrote well.` → 2,
`It was 3.14, e.g. pi. Really.` → 2, `Wait . . . Really?` → 2, and
the final story → 2. Known limit: a sentence genuinely ending in the
pronoun "I" (e.g. "...than I.") would be skipped as an initial — not
present in this story, and accepted as a trade-off of the heuristic.

Re-test after the edit (same command, fresh output dir):

```text
OK: wrote /tmp/horror-revise-out/entry.txt
characters: 212 (max 400)
sentences: 2
bytes: 212
read-back: byte-for-byte identical
```

Output is byte-for-byte identical to the pre-revision run (sha256
`fade1c83e8ee9640e65608c882f6e1c9114a68146268ded33948cf667210acd1`
before and after). Story text, 212 characters, and 2 sentences
unchanged. LICENSE, README.md, and `.makefun/freshness.json`
untouched. Not committed — the coordinator handles commit/push.

## Files

- `main.py` — entry program (Python stdlib only)
- `README.md` — bounty link + badges
- `BUILD-REPORT.md` — this report
- `LICENSE` — MIT (anchor, untouched)
- `.makefun/freshness.json` — anchor, untouched

Not committed — the coordinator handles commit/push.
