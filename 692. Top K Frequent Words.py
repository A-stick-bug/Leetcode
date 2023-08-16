from typing import List
from collections import Counter


def topKFrequent(words: List[str], k: int) -> List[str]:
    words.sort()  # sort lexicographically
    new_words = Counter(words)
    res = new_words.most_common(k)
    return list(map(lambda x: x[0], res))


print(topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k=4))
