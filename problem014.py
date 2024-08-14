class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt=0
        for i in range(len(nums)):
            nums[i]=nums[i]%3
            if nums[i]!=0:
                cnt+=1
        return cnt