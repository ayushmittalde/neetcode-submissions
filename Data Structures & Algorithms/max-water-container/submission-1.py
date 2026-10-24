class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        maxwater=0
        while (l<r):
            temp=min(heights[l],heights[r])*(r-l)
            maxwater=max(maxwater,temp)
            if (heights[l]<heights[r]):
                l+=1
            else :
                r-=1
        print( l ,r)
        return maxwater
        