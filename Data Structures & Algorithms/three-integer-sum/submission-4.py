

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol=[]
        nums.sort()
        length=len(nums)
        i=0
        while (i<length):
            l,r=i+1,length-1

            while(l<r):
                if nums[l]+nums[r]+nums[i]==0:
                    sol.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1

                    while (nums[l]==nums[l-1]) and l<r:
                        l+=1

                elif nums[l]+nums[r]+nums[i]>0:
                    r-=1
                elif nums[l]+nums[r]+nums[i]<0:
                    l+=1
                
            i+=1
            while (i<length and nums[i]==nums[i-1]):
                i+=1

        return sol