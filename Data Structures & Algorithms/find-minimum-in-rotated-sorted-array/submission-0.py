class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while (l<r):
            x=(l+r)>>1

            if nums[r]>nums[x] and nums [l]>nums[x]:
                r=x
            elif nums[r]<nums[x] and nums [l]<=nums[x]:
                l=x+1
            elif nums[l]<=nums[x] and nums[x]<nums[r]:
                r=x
            
        return nums[r]        