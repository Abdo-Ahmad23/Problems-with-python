class Solution:
    def get_subsets(arr):
        n = len(arr)
        subsets = []

        for bitmask in range(1 << n):
            subset = list()
            for i in range(n):
                if bitmask & (1 << i):
                    subset.append(arr[i])
            subsets.append(subset)

        return subsets

    def subsetXORSum(self, nums: List[int]) -> int:
        my_list = Solution.get_subsets(nums)
        sum = 0
        for i in range(len(my_list)):
            x = 0
            for j in range(len(my_list[i])):
                x ^= my_list[i][j]
            if len(my_list[i]) > 0:
                sum += x
        return sum