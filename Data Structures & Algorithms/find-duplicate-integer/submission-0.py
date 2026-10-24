class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x=set()

        for i,val in enumerate(nums):
            if val in x:
                return val
            else:
                x.add(val)
    
        return None
        