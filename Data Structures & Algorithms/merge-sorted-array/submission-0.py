class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        i=m-1
        j=n-1
        k=m+n-1

        while k>-1 and i>-1 and j>-1:
            if nums1[i]>=nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            elif nums1[i]<nums2[j]:
                nums1[k]=nums2[j]
                j-=1
            
            k-=1
        
        if i==-1 and j>-1 and k>-1:
            for m in range(j,-1,-1):
                nums1[k]=nums2[m]
                k-=1
        """
        Do not return anything, modify nums1 in-place instead.
        """
        