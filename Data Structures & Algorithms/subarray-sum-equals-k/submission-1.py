class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        rightsum=0
        store={}
        store[0]=1
        count=0

        for i in range(len(nums)-1,-1,-1):
            rightsum+=nums[i]
            count+=store.get(rightsum-k,0)
            store[rightsum]=store.get(rightsum,0)+1
        
        return count