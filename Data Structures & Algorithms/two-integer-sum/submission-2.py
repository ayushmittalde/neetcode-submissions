class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = list()
        last = len(nums)
        for i in range(len(nums)):
            find=target-nums[i]
            temp=i+1
            while temp < last:
                if nums[temp]==find:
                    x.append(i)
                    x.append(temp)
                    return x
                else :
                    temp+=1
                


        