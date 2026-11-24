#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun bounty u-suroto-two-sentence-horror-acea9253.

Writes exactly one two-sentence horror story (<= 400 characters) to
/output/entry.txt, atomically (temp file + rename), then reads it back
byte-for-byte and verifies it.

Standard library only. No network, no dependencies.

The output directory defaults to /output (the sandbox path) and can be
overridden for local testing with the OUTPUT_DIR environment variable.
"""

import os
import re
import sys
import tempfile

STORY = (
    "The previous owners had no children, yet the nursery was painted "
    "pale yellow and smelled faintly of milk. "
    "This morning I found my daughter's name written in the dust beneath "
    "the window; we haven't chosen one yet."
)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

MAX_CHARS = 400


def count_sentences(text):
    """Count sentences by terminal punctuation followed by space or end."""
    return len(re.findall(r"[.!?](?:\s|$)", text))


def verify(text):
    """Check the story against the bounty gate. Returns a list of problems."""
    problems = []
    if not text.strip():
        problems.append("empty or whitespace-only")
    if len(text) != len(text.strip()):
        problems.append("leading/trailing whitespace")
    if not 1 <= len(text) <= MAX_CHARS:
        problems.append("length %d chars, must be 1-%d" % (len(text), MAX_CHARS))
    n = count_sentences(text)
    if n != 2:
        problems.append("sentence count %d, must be exactly 2" % n)
    return problems


def main():
    problems = verify(STORY)
    if problems:
        for p in problems:
            print("FAIL: %s" % p, file=sys.stderr)
        return 1

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    data = STORY.encode("utf-8")

    # Atomic write: temp file in the same directory, then rename.
    fd, tmp_path = tempfile.mkstemp(
        dir=OUTPUT_DIR, prefix=".entry.", suffix=".tmp"
    )
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_path, OUTPUT_PATH)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise

    # Read-back verification, byte-for-byte.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != data:
        print("FAIL: read-back mismatch", file=sys.stderr)
        return 1
    roundtrip = written.decode("utf-8")
    problems = verify(roundtrip)
    if problems:
        for p in problems:
            print("FAIL after write: %s" % p, file=sys.stderr)
        return 1

    print("OK: wrote %s" % OUTPUT_PATH)
    print("characters: %d (max %d)" % (len(STORY), MAX_CHARS))
    print("sentences: %d" % count_sentences(STORY))
    print("bytes: %d" % len(data))
    print("read-back: byte-for-byte identical")
    print()
    print(STORY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
