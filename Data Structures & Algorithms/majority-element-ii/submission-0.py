from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        length =len(nums)// 3
        res=[]
        x=Counter(nums)

        for val,freq in x.items():
            if freq>length :
                res.append(val)
        
        return res

        