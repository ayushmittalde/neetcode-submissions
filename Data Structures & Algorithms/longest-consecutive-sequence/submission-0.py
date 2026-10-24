class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements= set(nums)
        start=[]
        sol=0
        for i in nums:
            if ((i-1) not in elements):
                start.append(i)
        
        for x in start:
            temp=1
            while (x+1 in elements):
                temp+=1
                x+=1

            if temp > sol:
                sol=temp

        return sol