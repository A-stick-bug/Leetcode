# simple binary index tree operations: how to query and update

from typing import List


class FenwickTree:  # uses 1-indexing
    def __init__(self, nums: list[int]):
        """Create a Fenwick tree from an array by adding elements one by one"""
        self.bit = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):  # create binary index tree by using update on each element
            self.update(i + 1, num)

    def update(self, i: int, val: int) -> None:
        """Add val to self.bit[i]"""
        while i < len(self.bit):
            self.bit[i] += val
            i += i & (-i)

    def query(self, i: int):
        """Get the sum up to the i-th element (inclusive)"""
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= i & (-i)
        return total


class NumArray:  # queries are 0-indexed, BIT is 1-indexed
    def __init__(self, nums: List[int]):
        self.nums = nums  # store a copy of the original array for quicker updates
        self.bit = FenwickTree(nums)

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]  # to change the i-th element to val, we must add (new_val - cur_val) to it
        self.bit.update(index + 1, diff)  # +1 because the BIT uses 1-indexing
        self.nums[index] = val  # update original array

    def sumRange(self, left: int, right: int) -> int:
        return self.bit.query(right + 1) - self.bit.query(left)


test = NumArray([1, 2, 3])
print(test.sumRange(0, 2))  # return 1 + 3 + 5 = 9
test.update(1, 2)  # nums = [1, 2, 5]
print(test.sumRange(0, 2))  # return 1 + 2 + 5 = 8
