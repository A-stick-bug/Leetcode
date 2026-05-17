# https://leetcode.com/problems/implement-rand10-using-rand7/description/
# Split by case:
# We think of 10 = 2 * 5 and generate each part independently
# i.e. pair up [0,5] X [1,2,3,4,5] -> uniform [1,2,...,10], as each number can be formed in 1 way
#
# uses 67/30 ~ 2.333 calls on averages
# branch 1: 5/7 chance of using 7/6 moves
# branch 2: 2/7 chance of using 7/5 moves
# total: 1 + 5/7 * 7/6 + 2/7 * 7/5 = 1 + 5/6 + 2/5 = 67/30

from random import randint


# The rand7() API is already defined for you.
def rand7(): return randint(1, 7)


# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """

        # expected 67/30
        first = rand7()
        res = 0
        if first <= 5:  # use for unit
            res += first
            second = rand7()
            while second == 7:  # 6/7 success chance, expect 7/6 tries
                second = rand7()
            res += 5 * (second % 2)
        else:  # use for x5
            res += 5 if first == 6 else 0
            second = rand7()
            while second > 5:  # 5/7 success chance, expect 7/5 tries
                second = rand7()
            res += second

        return res
