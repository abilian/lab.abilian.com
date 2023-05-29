import re
import sys
from collections import Counter

import nltk
import nltk.corpus
from attr import define
from devtools import debug
from nltk import TreebankWordTokenizer, sent_tokenize
from pytrends.request import TrendReq


@define
class KeywordsGenerator:
    pytrends: TrendReq

    def generate_tags(self, file_path, top_words=30):
        file_text = self._get_file_contents(file_path)
        clean_words = self.get_clean_words(file_text)

        word_counter = Counter(clean_words)

        for word, _count in word_counter.most_common(top_words):
            try:
                suggestions = self.get_suggestions(word)
                word_counter.update(suggestions)
            except Exception as e:
                print(e)

        debug(word_counter.most_common(30))

        tags = [x[0] for x in word_counter.most_common(30)]
        debug(tags)
        return ", ".join(list(set(tags)))

    def get_clean_words(self, text) -> list[str]:
        # 1. Convert Text To Lowercase and remove numbers
        lower_case_text = str.lower(text)
        just_text = re.sub(r"\d+", "", lower_case_text)

        # 2. Tokenise Paragraphs To words
        list = sent_tokenize(just_text)
        tokenizer = TreebankWordTokenizer()
        tokens = tokenizer.tokenize(just_text)

        # 3. Clean text
        clean = self._clean_tokens(tokens)
        return clean

    def _clean_tokens(self, tokens: list[str]) -> list[str]:

        def is_clean(w: str) -> bool:
            return not self.is_stopword(w) and 2 < len(w) < 20 and w.isalpha()

        return [w for w in tokens if is_clean(w)]

    def is_stopword(self, word):
        stopwords = nltk.corpus.stopwords.words("english")
        return word in stopwords

    def get_suggestions(self, keyword):
        print(f"Searching pytrends for {keyword}")
        self.pytrends.build_payload([keyword], timeframe="today 12-m")
        data = self.pytrends.related_queries()[keyword]["top"]
        debug(data)

        if data is None or data.values is None:
            return []

        result = []
        for x in data.values.tolist():
            word = x[0]
            if not self.is_stopword(word):
                result.append(word)

        debug(result)
        return result

    def _get_file_contents(self, file_path):
        return open(file_path, "r", encoding="utf-8", errors="ignore").read()

    def _get_top_words(self, words, top):
        counter = Counter(words)
        return [t[0] for t in counter.most_common(top)]


def process_file(file_path):
    pytrends = TrendReq(hl="en-GB")
    tags = KeywordsGenerator(pytrends).generate_tags(file_path)
    print(tags)


if __name__ == "__main__":
    nltk.download("punkt")
    nltk.download("stopwords")

    for file_path in sys.argv[1:]:
        process_file(file_path)
