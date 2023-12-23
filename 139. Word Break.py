# dfs with memoization to prevent repeating states

from functools import cache


def wordBreak(s: str, wordDict: list[str]) -> bool:
    @cache
    def solve(cur: str):
        if cur == s:  # matched the string
            return True

        for word in wordDict:
            new_word = cur + word
            if s.startswith(new_word) and solve(new_word):  # if we are on the right path, go deeper
                return True
        return False

    return solve("")


print(wordBreak(s="cog", wordDict=["co", "g"]))
