class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        y=len(heights)
        smallerleft=[-1]*y
        stack=[]
        maxa=-1

        for i in range(y):
            while stack and heights[i]<=heights[stack[-1]]:
                stack.pop()

            if stack:
                smallerleft[i]=stack[-1]
            
            stack.append(i)
        
        stack.clear()

        for i in range(y-1,-1,-1):

            while stack and heights[i]<=heights[stack[-1]]:
                stack.pop()

            if stack:
                area= heights[i]*(stack[-1]-smallerleft[i]-1)
                maxa=max(area,maxa)
            else:
                area= heights[i]*(y-smallerleft[i]-1)
                maxa=max(area,maxa)
            
            stack.append(i)

        return maxa