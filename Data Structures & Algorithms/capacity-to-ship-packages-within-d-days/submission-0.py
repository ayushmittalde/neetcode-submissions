class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        minw=r

        while (l<=r):
            mid=(l+r)>>1
            count=1
            sumx=0
            for w in weights:
                sumx+=w
                if sumx>mid:
                    count+=1
                    sumx=w
            
            if count <= days:
                minw=min(minw,mid)
                r=mid-1
            else:
                l=mid+1
        
        return minw