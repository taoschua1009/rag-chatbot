import os
import re
import unicodedata
from pathlib import Path


INPUT_DIR = Path(r"C:\work\chunking-doc\articles_md_raw")
OUTPUT_DIR = Path(r"C:\work\chunking-doc\split_md")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SKIP_KEYWORDS = [
    "that's all", "that’s all", "congratulations", "thank you", "thanks", "good luck"
]


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    replacements = {
        "’": "'", "‘": "'", "“": '"', "”": '"', "…": "...",
        "\u00A0": " ",  # non-breaking space
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text


def slugify(text):
    text = normalize_text(text.lower())
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"\s+", "-", text.strip())


def should_skip_heading(heading: str) -> bool:
    heading = normalize_text(heading).lower()
    return any(kw in heading for kw in SKIP_KEYWORDS)


def split_markdown_sections(md_text: str):
    pattern = r'^(#{1,6} .*)'
    lines = normalize_text(md_text).splitlines()

    sections = []
    current_section = []
    current_title = None

    for line in lines:
        if re.match(pattern, line):
            if current_section and current_title and not should_skip_heading(current_title):
                sections.append((current_title, "\n".join(current_section).strip()))
            current_section = []
            current_title = line.strip()
        current_section.append(line)

    if current_section and current_title and not should_skip_heading(current_title):
        sections.append((current_title, "\n".join(current_section).strip()))

    return sections


def process_file(md_file: Path):
    with md_file.open("r", encoding="utf-8") as f:
        content = f.read()

    
    url_match = re.search(r"Article URL:\s*(https?://\S+)", content)
    article_url = url_match.group(1).strip() if url_match else ""

    
    content_wo_url = re.sub(r"---\s*Article URL:.*", "", content, flags=re.DOTALL).strip()

    parts = split_markdown_sections(content_wo_url)
    base_slug = md_file.stem

    for idx, (title, section) in enumerate(parts):
        title_slug = slugify(title)[:50] if title else f"part-{idx+1}"
        out_filename = f"{base_slug}--{title_slug}.md"
        out_path = OUTPUT_DIR / out_filename

        
        if article_url:
            footer = f"For additional information, see the full article [here]({article_url})\n\n---"
        else:
            footer = "---"

        full_text = f"{section.strip()}\n\n{footer}"

        with out_path.open("w", encoding="utf-8") as out:
            out.write(full_text.strip() + "\n")

        print(f" {md_file.name} → {out_filename}")


def main():
    md_files = list(INPUT_DIR.glob("*.md"))
    if not md_files:
        print("No .md files found in the directory.")
        return

    for md_file in md_files:
        process_file(md_file)

    print(f"\n Processed {len(md_files)} files → Results saved at: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()

