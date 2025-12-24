import json
from pathlib import Path

# ✅ EXACT DOCS PATH
DOCS_PATH = Path(r"C:\Users\HAFIZ ATIQ\physical-ai-book\docs\physical-ai-book")
OUTPUT_FILE = Path(__file__).parent / "chunks.json"

chunks = []

for md_file in DOCS_PATH.rglob("*.md"):
    try:
        text = md_file.read_text(encoding="utf-8").strip()
        if not text:
            continue

        chunks.append({
            "source": str(md_file.relative_to(DOCS_PATH)),
            "content": text
        })
    except Exception as e:
        print(f"❌ Failed to read {md_file}: {e}")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(chunks, f, indent=2, ensure_ascii=False)

print(f"✅ Ingested {len(chunks)} markdown files")
print(f"📁 Source path: {DOCS_PATH}")
print(f"🧩 Output: {OUTPUT_FILE}")
