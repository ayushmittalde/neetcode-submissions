class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        seen=set()

        for i in nums:
            if i not in seen:
                nums[k]=i
                seen.add(i)
                k+=1
        
        return k