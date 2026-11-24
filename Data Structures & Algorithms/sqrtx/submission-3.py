class Solution:
    def mySqrt(self, x: int) -> int:
        l=1
        r=max(x//2,1)

        while (l<=r):
            mid=(l+r)>>1
            squ =mid*mid
            if squ == x:
                return mid
            elif squ> x:
                r=mid-1
            else:
                l=mid+1
        
        return r