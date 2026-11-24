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

## Files

- `main.py` — entry program (Python stdlib only)
- `README.md` — bounty link + badges
- `BUILD-REPORT.md` — this report
- `LICENSE` — MIT (anchor, untouched)
- `.makefun/freshness.json` — anchor, untouched

Not committed — the coordinator handles commit/push.
