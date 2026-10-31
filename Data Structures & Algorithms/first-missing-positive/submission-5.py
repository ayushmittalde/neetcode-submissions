class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        x=[0]*(len(nums)+2)

        for i in nums:
            if 1<=i<=len(nums):
                x[i]=1
        
        for i in range(1,len(nums)+2):
            if x[i]!=1:
                return i