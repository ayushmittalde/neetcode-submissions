class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = list()
        v= {}
        last = len(nums)
        for index, value in enumerate (nums):
            find = target-value
            temp = nums[index+1:]
            if find in temp:
                return [index,temp.index(find)+index+1]
        
        return 

                


        