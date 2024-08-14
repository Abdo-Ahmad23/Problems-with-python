class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        x = start
        for i in range(1, n):
            sum = start + i * 2
            x ^= sum
        return x