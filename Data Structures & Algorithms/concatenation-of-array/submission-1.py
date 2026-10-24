class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for x in nums[:]:
            nums.append(x)
        
        return nums
        