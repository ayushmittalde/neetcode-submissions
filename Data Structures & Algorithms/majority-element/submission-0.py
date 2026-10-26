class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l=len(nums)
        th=l>>1 # divide by 2
        count={}

        for i in range(l):
            el=nums[i]
            count[el]=count.get(el,0)+1
            if count[el]>th:
                return el
