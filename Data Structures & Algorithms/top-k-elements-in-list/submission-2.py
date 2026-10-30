class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in range(len(nums)):
            count[nums[i]]=count.get(nums[i],0)+1
        
        freq=[[] for _ in range(len(nums)+1)]

        for val,c in count.items():
            freq[c].append(val)
        
        res=[]
        last= len(nums)
        
        while len(res)<k:
            res.extend(freq[last])
            last-=1

        return res