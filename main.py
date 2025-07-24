import subprocess
import sys
import json
from pathlib import Path
import hashlib

STATE_FILE = Path("article_state.json")
RAW_DIR = Path("articles_md_raw")
LOG_FILE = Path("job_log.json")

def hash_file_content(file_path: Path) -> str:
    
    content = file_path.read_text(encoding="utf-8")
    return hashlib.md5(content.encode("utf-8")).hexdigest()

def detect_changes():
    if not STATE_FILE.exists():
        return [], []

    old_state = json.loads(STATE_FILE.read_text(encoding="utf-8"))
    added, updated = [], []

    for md_file in RAW_DIR.glob("*.md"):
        slug = md_file.stem
        hash_now = hash_file_content(md_file)
        if slug not in old_state:
            added.append(slug)
        elif old_state[slug] != hash_now:
            updated.append(slug)

    return added, updated

def update_state():
    state = {}
    for md_file in RAW_DIR.glob("*.md"):
        slug = md_file.stem
        state[slug] = hash_file_content(md_file)
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")

def run_script(script_name):
    print(f"\n Running: {script_name}")
    result = subprocess.run([sys.executable, script_name], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(f" Error in {script_name}:\n{result.stderr}")

def main():
    print(" STARTING daily RAG job...")

    # 1. Scrape
    run_script("scrape.py")

    # 2. Detect delta
    added, updated = detect_changes()
    skipped = [f.stem for f in RAW_DIR.glob("*.md") if f.stem not in added + updated]

    log = {
        "added": added,
        "updated": updated,
        "skipped": skipped
    }
    LOG_FILE.write_text(json.dumps(log, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f" Added: {len(added)} |  Updated: {len(updated)} |  Skipped: {len(skipped)}")
    print(f" Log saved: {LOG_FILE}")

    if added or updated:
        # 3. Chunk & upload only if something changed
        run_script("chunking5.py")
        run_script("upload.py")
        update_state()
    else:
        print(" No new or updated articles → skip chunking & upload.")

if __name__ == "__main__":
    main()
