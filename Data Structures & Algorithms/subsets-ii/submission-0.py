class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        temp=[]
        sol=[]
        nums.sort()
        lenx=len(nums)
        def subset(idx,temp):
            nonlocal lenx
            if idx>=lenx:
                sol.append(temp.copy())
                return 
            
            temp.append(nums[idx])
            subset(idx+1,temp)
            temp.pop()
            while(idx+1<lenx and nums[idx]==nums[idx+1]):
                idx+=1
            subset(idx+1,temp)
        
        subset(0,temp)
        return sol
            
        