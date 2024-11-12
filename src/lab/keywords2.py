import sys
from pathlib import Path

from keybert import KeyBERT
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-mpnet-base-v2")

kw_model = KeyBERT(model=model)

ROOT = Path("/Users/fermigier/Documents/Vaults/Notes/Public")


def process_file(file_path: Path):
    document = file_path.read_text()
    if "<!-- Keywords -->" in document:
        print("Already processed")
        return
    keywords = kw_model.extract_keywords(document)
    keywords = [f"#{kw}" for kw, w in keywords if w > 0.4]

    document = document.rstrip()
    document += "\n\n<!-- Keywords -->\n"
    document += " ".join(keywords)
    document += "\n<!-- /Keywords -->\n"
    file_path.write_text(document)


def main():
    if len(sys.argv) < 2:
        files = ROOT.rglob("*.md")
    else:
        files = [Path(file_path) for file_path in sys.argv[1:]]

    for path in files:
        print(str(path))
        process_file(path)
        print()


if __name__ == "__main__":
    main()
