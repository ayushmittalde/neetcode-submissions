class Solution:
    def binarysearch(self,nums,target):
        l=0
        r=len(nums)-1

        while(l<=r):
            mid=(l+r)>>1

            if nums[mid]==target:
                return True
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l=0
        r=len(matrix)-1

        while (l<=r):

            mid=(l+r)>>1
            if target< matrix[mid][0] :
                r=mid-1
            elif target >matrix[mid][-1]:
                l=mid+1
            else:
                return self.binarysearch(matrix[mid],target)
        
        return False