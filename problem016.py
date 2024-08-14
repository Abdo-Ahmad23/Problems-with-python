class Solution:
    def sum_natural_numbers(n):
        return n * (n + 1) // 2

    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = {}
        cnt = 0
        st = set()
        for i in range(len(nums)):
            st.add(nums[i])
            dic[nums[i]] = 0
        for i in range(len(nums)):
            dic[nums[i]] += 1
        for i in st:
            cnt += Solution.sum_natural_numbers(dic[i] - 1)
        return cnt

