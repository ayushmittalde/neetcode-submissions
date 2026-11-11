class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        sol=[]
        nl=len(nums)
        for i in range(nl):

            if i>0 and nums[i]==nums[i-1]:
                continue
            
            for j in range(i+1,nl):
                if j!=(i+1) and nums[j]==nums[j-1]:
                    continue 

                l=j+1 
                r=nl-1

                while(l<r):
                    tg = nums[i]+nums[j]+nums[l]+nums[r]

                    if target == tg :
                        sol.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1

                        while (l<r and nums[l]==nums[l-1]):
                            l+=1

                    elif tg > target :
                        r-=1
                    elif tg < target :
                        l+=1

        return sol