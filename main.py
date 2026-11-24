"""Famous Last Words at 1 Percent — make.fun entry (account B / Slothana).

Writes the phone's one-line farewell to /output/entry.txt.
Deterministic, stdlib only, no network, no secrets, no input files:
two runs produce byte-identical output.
"""

from pathlib import Path

# The line: the phone tries to negotiate for one more percent — deleting
# the embarrassing shower-singing photos in exchange — then dies
# mid-sentence, mid-word, before it can finish the thought.
LAST_WORDS = (
    "Deal: I'll trade you one more percent if you delete those photos "
    "of you singing in the shower \u2014 actually, never mind, I'm already go\u2014"
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 199


def verify(text: str) -> str:
    """Check the gate: UTF-8 text, 1-199 chars, a single non-blank line."""
    line = text.strip()
    if not line:
        raise ValueError("entry is blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} cap")
    return line


def write_entry(path: Path = OUTPUT_PATH) -> str:
    """Write the verified line to the output path and return it."""
    line = verify(LAST_WORDS)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(line, encoding="utf-8")
    return line


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
