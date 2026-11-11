class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        maxar=0
        while (l<r):

            if heights[l]>=heights[r]:
                maxar=max(maxar,(r-l)*heights[r])
                r-=1
    
            else:
                maxar=max(maxar,(r-l)*heights[l])
                l+=1


        return maxar