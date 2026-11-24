"""One Emoji, One Smile - a make.fun entry.

Writes exactly one emoji, the melting face, to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR or /output), with no trailing newline.
"""

import os

TEXT = "🫠"


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

    # Self-check: the gate wants UTF-8 text of 1 to 8 characters, and this
    # entry is exactly one emoji - a single code point - whose bytes on
    # disk must be exactly TEXT encoded as UTF-8 (no trailing newline).
    assert len(TEXT) == 1, "entry text must be exactly 1 code point"
    assert 1 <= len(TEXT) <= 8, "entry text must be 1-8 code points"
    with open(path, "rb") as f:
        written = f.read()
    assert written == TEXT.encode("utf-8"), "written bytes must equal TEXT exactly"


if __name__ == "__main__":
    main()
