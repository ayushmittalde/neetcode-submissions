class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        y=len(nums)
        ans=[0]*(y*2)

        for i in range(y):
            ans[i]=nums[i]
            ans[y+i]=nums[i]
        
        return ans