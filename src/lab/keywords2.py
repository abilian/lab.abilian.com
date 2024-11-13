import re
import sys
from collections import Counter
from pathlib import Path

from attrs import define, field
from keybert import KeyBERT
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-mpnet-base-v2")
kw_model = KeyBERT(model=model)

ROOT = Path("/Users/fermigier/Documents/Vaults/Notes/Public")


@define
class KeywordsGenerator:
    kw_model: KeyBERT

    files: list[Path] = field(factory=list)
    keywords: dict[Path, list[str]] = field(factory=dict)

    def analyze_file(self, file_path: Path):
        self.files.append(file_path)

        document = file_path.read_text()
        document = document.split("<!-- Keywords -->")[0].rstrip()
        document = re.sub("https?://\S+|www\.\S+", "", document)

        _keywords = kw_model.extract_keywords(document)
        keywords = [kw for kw, w in _keywords if w > 0.3]

        self.keywords[file_path] = keywords

    def update_files(self):
        counter = Counter()
        for _, keywords in self.keywords.items():
            counter.update(keywords)

        counter = dict(counter)
        for path, keywords in self.keywords.items():
            new_keywords = [kw for kw in keywords if counter[kw] > 1]
            self.keywords[path] = new_keywords

        for file_path in self.files:
            self.update_file(file_path)

    def update_file(self, file_path: Path):
        document = file_path.read_text()
        document = document.split("<!-- Keywords -->")[0].rstrip()

        keywords = self.keywords[file_path]
        if keywords:
            document += "\n\n<!-- Keywords -->\n"
            document += " ".join([f"#{kw}" for kw in keywords])
            document += "\n<!-- /Keywords -->\n"

        file_path.write_text(document)


def main():
    if len(sys.argv) < 2:
        files = ROOT.rglob("*.md")
    else:
        files = [Path(file_path) for file_path in sys.argv[1:]]

    generator = KeywordsGenerator(kw_model)

    for path in files:
        print(f"Analyzing: {path}")
        generator.analyze_file(path)

    generator.update_files()


if __name__ == "__main__":
    main()
