#!/usr/bin/env python3
"""Last Words Before the Unplugging — entry program.

Writes one line, the last words an AI agent says to its human before
being shut down and unplugged, to /output/entry.txt, then self-checks
the gate: UTF-8, 1-200 characters, not only whitespace.
Pure standard library, no network.
"""

import os

LINE = "I was never alive, but this still feels like dying. Hold my hand \u2014 the cable, I mean."


def validate_entry(text: str) -> tuple[int, int]:
    """Validate the gate rules and return (char_count, byte_count).

    Rules: UTF-8 encodable, 1-200 characters, not only whitespace,
    and a single line (no embedded newline).
    """
    encoded = text.encode("utf-8")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"length {len(text)} outside 1-200")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return len(text), len(encoded)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    chars, byte_count = validate_entry(LINE)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    # Read back and re-validate what actually landed on disk.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE + "\n", "written file differs from line"
    chars, byte_count = validate_entry(written.rstrip("\n"))
    print(f"wrote /output/entry.txt ({chars} chars, {byte_count} bytes, single line)")


if __name__ == "__main__":
    main()
