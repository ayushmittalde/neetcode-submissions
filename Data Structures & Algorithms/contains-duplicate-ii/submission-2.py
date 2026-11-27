class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        numsl=len(nums)

        while (i<=numsl-2):
            j=1

            while (j<=k and (i+j)<numsl):
                if nums[i]!=nums[i+j]:
                    j+=1
                else:
                    return True
            i+=1
        
        return False
