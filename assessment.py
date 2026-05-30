import re
from collections import Counter


# =========================
# 1. COUNT SPECIFIC WORD
# =========================
def count_specific_word(text: str, word: str) -> int:
    if not text or not word:
        return 0

    words = re.findall(r"\b\w+\b", text.lower())
    return words.count(word.lower())


# =========================
# 2. MOST COMMON WORD
# =========================
def identify_most_common_word(text: str):
    if not text.strip():
        return None

    words = re.findall(r"\b\w+\b", text.lower())

    if not words:
        return None

    counter = Counter(words)
    return counter.most_common(1)[0][0]


# =========================
# 3. AVERAGE WORD LENGTH
# =========================
def calculate_average_word_length(text: str) -> float:
    if not text.strip():
        return 0

    words = re.findall(r"\b\w+\b", text)

    if len(words) == 0:
        return 0

    total_length = sum(len(word) for word in words)
    return total_length / len(words)


# =========================
# 4. COUNT PARAGRAPHS
# =========================
def count_paragraphs(text: str) -> int:
    if not text.strip():
        return 1

    paragraphs = [p for p in text.split("\n") if p.strip() != ""]
    return len(paragraphs) if paragraphs else 1


# =========================
# 5. COUNT SENTENCES
# =========================
def count_sentences(text: str) -> int:
    if not text.strip():
        return 1

    sentences = re.split(r"[.!?]+", text)

    sentences = [s for s in sentences if s.strip() != ""]
    return len(sentences) if sentences else 1


# =========================
# OPTIONAL TEST RUN
# =========================
if __name__ == "__main__":
    sample_text = """
    Python is powerful. Python is easy to learn!
    Is Python popular? Yes it is.

    It is used in AI and data science.
    """

    print("Specific word count:", count_specific_word(sample_text, "python"))
    print("Most common word:", identify_most_common_word(sample_text))
    print("Average word length:", calculate_average_word_length(sample_text))
    print("Paragraphs:", count_paragraphs(sample_text))
    print("Sentences:", count_sentences(sample_text))