class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        sol=[]
        tempx=[]
        lenx=len(nums)

        def traverse(idx):
            nonlocal lenx
            if idx ==lenx:
                sol.append(tempx.copy())
                return
            
            traverse(idx+1)
            tempx.append(nums[idx])
            traverse(idx+1)
            tempx.pop()
        
        traverse(0)
        return sol



        