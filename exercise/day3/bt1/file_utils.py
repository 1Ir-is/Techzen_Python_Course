from typing import Dict

def read_file_content(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def count_word_frequency(text: str) -> Dict[str, int]:
    text = text.lower()
    for p in ".,;:?!()[]":
        text = text.replace(p, "")
    words = [w for w in text.split() if w]
    freq: Dict[str, int] = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq