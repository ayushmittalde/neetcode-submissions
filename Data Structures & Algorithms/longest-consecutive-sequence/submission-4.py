class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums)==0):
            return 0

        lookup=set(nums)
        maxlen=1
        count =0
        for i in nums:
            if i-1 not in lookup:
                count=1
                cand=i
                while cand+1 in lookup:
                    count+=1
                    cand+=1
                maxlen=max(count,maxlen)
        return maxlen 