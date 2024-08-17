class Solution:
    def sum_of_multiples_of(n, m):
        k = n // m
        return m * k * (k + 1) // 2

    def sumOfMultiples(self, n: int) -> int:
        sum_3 = Solution.sum_of_multiples_of(n, 3)
        sum_5 = Solution.sum_of_multiples_of(n, 5)
        sum_7 = Solution.sum_of_multiples_of(n, 7)
        sum_15 = Solution.sum_of_multiples_of(n, 15)
        sum_21 = Solution.sum_of_multiples_of(n, 21)
        sum_35 = Solution.sum_of_multiples_of(n, 35)
        sum_105 = Solution.sum_of_multiples_of(n, 105)

        result = sum_3 + sum_5 + sum_7 - sum_15 - sum_21 - sum_35 + sum_105
        return result

sol=Solution()
print(sol.sumOfMultiples(3))