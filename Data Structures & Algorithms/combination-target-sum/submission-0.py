class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        sol=[]
        temp=[]
        lenx=len(nums)

        def trysum(sumx,idx):            
            for i in range(idx,lenx):
                sumx+=nums[i]
                temp.append(nums[i])
                if sumx==target:
                    sol.append(temp.copy())
                elif sumx<target:
                    trysum(sumx,i)
                
                temp.pop()
                sumx-=nums[i]

        trysum(0,0)

        return sol.copy()