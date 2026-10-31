class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)

        i=0
        while(i<n):
            cand=nums[i]
            if 1<=cand<=n and nums[cand-1]!=nums[i]:    
                nums[cand-1], nums[i]=nums[i],nums[cand-1]
                continue
            i+=1

        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        
        return n+1