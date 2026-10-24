class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sumx=sum(x for x in piles)
        l=1
        r=max(piles)
        sol=0
        while (l<=r):
            hours=0
            temp=(l+r)//2
            for x in piles:
                hours+=math.ceil(x/temp)
            if (hours > h):
                l=temp+1
            else :
                print("exe")
                sol=temp
                r=temp-1

        return sol
        
        

        