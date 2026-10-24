class Solution:
    def trap(self, height: List[int]) -> int:
        last = len(height)
        l=0
        r=1
        total = 0
        remove = 0
        leftmax=[0]*len(height)
        rightmax=[0]*len(height)

        for i in range (1,len(height)):
            if (leftmax[i-1]<=height[i-1]):
                leftmax[i]=height[i-1]
            else :
                leftmax[i]=leftmax[i-1]
        
        for i in range (len(height)-2,-1,-1):
            if (rightmax[i+1]<=height[i+1]):
                rightmax[i]=height[i+1]
            else :
                rightmax[i]=rightmax[i+1]
        
        total=0
        
        for i in range (len(height)):
            temp=(min(leftmax[i],rightmax[i]))-height[i]
            if (temp>0):
                total+=temp

        return total 

        