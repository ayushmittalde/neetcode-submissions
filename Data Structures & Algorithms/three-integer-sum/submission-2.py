class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        sol=[]
        x=len(nums)
        i=0

        while(i<x):

            l=i+1
            r=x-1

            while(l<r):
                target=nums[i]+nums[l]+nums[r]
                print(nums[i],nums[l],nums[r])
                if(target==0):
                    sol.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while(nums[l]==nums[l-1] and l<r):
                        l+=1

                elif(target>0):
                    r-=1
                elif(target<0):
                    l+=1

            a=nums[i]
            while (i<x and nums[i]==a):
                i+=1

        return sol