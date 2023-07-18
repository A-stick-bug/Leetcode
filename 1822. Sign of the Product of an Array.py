from typing import List

def arraySign(self, nums: List[int]) -> int:
    negatives = 0
    for i in nums:
        if i == 0:
            return 0
        elif i < 0:
            negatives += 1
    return 1 if negatives % 2 == 0 else -1