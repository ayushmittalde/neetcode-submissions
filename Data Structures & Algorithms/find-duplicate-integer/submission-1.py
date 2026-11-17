class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast=slow=0

        while True:
            slow=nums[slow]
            fast=nums[fast]
            fast=nums[fast]

            if fast==slow:
                break
        
        head2=0

        while head2!=slow:
            slow=nums[slow]
            head2=nums[head2]
        
        return slow