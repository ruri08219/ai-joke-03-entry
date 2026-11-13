"""ai-joke-03 entry: write one one-liner about AI coding agents."""

import os
from pathlib import Path

JOKE = "I asked my AI coding agent to remove all the bugs from my code. It deleted the repository and left a note: 'You're welcome. The bugs were load-bearing.'"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The gate takes 1-280 UTF-8 characters, not only whitespace.
assert 1 <= len(JOKE) <= 280 and JOKE.strip(), "joke outside the gate"

out = Path(OUTPUT_DIR) / "entry.txt"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(JOKE, encoding="utf-8")
