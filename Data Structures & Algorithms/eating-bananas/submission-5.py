import math as m
class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        r=max(piles)
        l=1
        minr=r
        while (l<=r):
            mid=(l+r)>>1
            hours=0

            for pile in piles:
                hours+=m.ceil(pile/mid)

            if hours <= h :
                minr=min(mid,minr)
                r=mid-1
            else:
                l=mid+1

        return minr
