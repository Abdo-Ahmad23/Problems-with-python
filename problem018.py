class Solution:
    def sum_of_divisibles(m, n):
        k = n // m
        total_sum = m * (k * (k + 1)) // 2

        return total_sum

    def sum_of_numbers(n):
        total_sum = n * (n + 1) // 2
        return total_sum

    def differenceOfSums(self, n: int, m: int) -> int:
        sum1 = Solution.sum_of_numbers(n) - Solution.sum_of_divisibles(m, n)
        return sum1 - Solution.sum_of_divisibles(m, n)