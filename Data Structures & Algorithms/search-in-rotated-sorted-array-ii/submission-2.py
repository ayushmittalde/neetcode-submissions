class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l=0
        r=len(nums)-1

        while l<r:
            mid=(l+r)>>1
            print(l,mid,r)

            if nums[mid]<nums[r]:
                r=mid
            elif nums[mid]>nums[r]:
                l=mid+1
            else:
                if nums[r-1]>nums[r]:
                    l= r
                    break
                r-=1
        
        point =l
        print (point)

        def bsearch(l:int,r:int)->int:

            while (l<=r):
                mid=(l+r)>>1

                if nums[mid]==target:
                    return True
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            
            return False

        
        if nums[point]<=target<=nums[-1]:
            return bsearch(point,len(nums)-1)
        else: return bsearch(0,point-1)