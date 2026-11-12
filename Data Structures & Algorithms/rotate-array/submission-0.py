class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nl=len(nums)
        sol=[-1]*nl

        for i in range(nl):
            index=(i+k)%nl
            sol[index]=nums[i]
        
        nums[:]=sol[:]
        """
        Do not return anything, modify nums in-place instead.
        """
        