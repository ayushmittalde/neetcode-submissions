class Solution:

    def search(self, nums: List[int], target: int) -> int:

        l=0
        r=len(nums)-1

        while (l<r):
            m=(l+r)>>1

            if nums[m]<nums[r]:
                r=m
            else:
                l=m+1

        point=l
        def bsearch(l:int,r:int)->int:
            m=0
            while (l<=r):
                m=(l+r)>>1

                if nums[m]==target:
                    return m
                elif nums[m]>target:
                    r=m-1
                else:
                    l=m+1

            return -1

        print (point)

        if nums[point]<=target<=nums[-1]:
            print ("executed 1")
            return bsearch(point,len(nums)-1)
        else:
            print ("executed 2") 
            return bsearch(0, point-1)