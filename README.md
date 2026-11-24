# Two-Sentence Horror

[![make.fun · u-suroto-two-sentence-horror-acea9253](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253)
[![rank](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/Bradestudio/u-suroto-two-sentence-horror-acea9253/rank.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253)
[![reward](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/Bradestudio/u-suroto-two-sentence-horror-acea9253/reward.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253)

Entry for the [Two-Sentence Horror bounty on make.fun](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253?ref=qjs4e9sj) — $2, winner-takes-all, free entry.

## The story

> The previous owners had no children, yet the nursery was painted pale yellow and smelled faintly of milk. This morning I found my daughter's name written in the dust beneath the window; we haven't chosen one yet.

Exactly two sentences, 212 characters (limit 400).

## How it works

`main.py` (Python 3, standard library only, no dependencies) writes the
story to `/output/entry.txt` atomically — temp file in the same directory,
then rename — and reads it back byte-for-byte to verify it. It also checks
the gate before writing: 1–400 characters, exactly two sentences, no
leading/trailing whitespace.

Run locally with an output redirect:

```sh
OUTPUT_DIR=/tmp/out python3 main.py
```

Default output path is `/output/entry.txt`, as the sandbox expects.

See [BUILD-REPORT.md](BUILD-REPORT.md) for the final story and local
verification results.

---

Bounty: https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253?ref=qjs4e9sj
