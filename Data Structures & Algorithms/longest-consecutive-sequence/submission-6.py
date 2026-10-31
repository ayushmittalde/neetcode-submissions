class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        lookup=set(nums)
        maxlen=0
        count =0
        for i in nums:
            if i-1 not in lookup:
                count=0
                cand=i
                while cand in lookup:
                    count+=1
                    cand+=1
                maxlen=max(count,maxlen)
        return maxlen 