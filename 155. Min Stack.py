# https://leetcode.com/problems/min-stack
# Monotonic stack
# Note: a simpler (and essentially equivalent) alternative is tracking the prefix sum

class MinStack:
    def __init__(self):
        self.stack = []
        self.minima = []  # monotonically decreasing, non strict

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minima or val <= self.minima[-1]:
            self.minima.append(val)

    def pop(self) -> None:
        removed = self.stack.pop()
        if removed == self.minima[-1]:
            self.minima.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minima[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
