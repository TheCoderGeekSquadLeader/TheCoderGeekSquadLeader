from pathlib import Path

README = Path("README.md")
MARKER = "<!-- keep-alive -->"

text = README.read_text(encoding="utf-8")

if MARKER in text:
    text = text.replace("\n" + MARKER, "").replace(MARKER, "")
else:
    text = text.rstrip("\n") + "\n" + MARKER + "\n"

README.write_text(text, encoding="utf-8")
