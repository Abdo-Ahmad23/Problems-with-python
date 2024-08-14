class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<=r:
                mid=(l+r)>>1
                if nums[mid]>nums[i]:
                    r=mid-1
                elif nums[mid]<nums[i]:
                    l=mid+1
                else:
                    return nums[mid]
                    
                