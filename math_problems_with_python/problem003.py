class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        m = 1
        sum = 0
        for i in s:
            sum += int(i)
            m *= int(i)
        return m - sum
