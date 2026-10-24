class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        sol=[[]]
        res=[]

        for val in nums :
            for perm in sol:
                for i in range(len(perm)+1):
                    temp=perm.copy()
                    temp.insert(i,val)
                    res.append(temp)
            sol=res.copy()
            res.clear()
        
        return sol


        