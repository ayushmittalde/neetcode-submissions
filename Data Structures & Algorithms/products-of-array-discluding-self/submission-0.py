class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prodright = [1]*len(nums)
        prodleft = [1]*len(nums)
        sol = [1]*len(nums)

        for i in range(len(nums)-2,-1,-1):
            prodright[i]=prodright[i+1]*nums[i+1]
        
        for i in range(1,len(nums)):
            prodleft[i]=prodleft[i-1]*nums[i-1]

        for i in range(len(nums)):
            sol[i]=prodleft[i]*prodright[i]

        return sol
