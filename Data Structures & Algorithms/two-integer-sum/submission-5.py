class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:

        hp={int:int}
        for i, v in enumerate(nums):
            if t-v in hp:
                return [hp[t-v],i]
            else:
                hp[v]=i
