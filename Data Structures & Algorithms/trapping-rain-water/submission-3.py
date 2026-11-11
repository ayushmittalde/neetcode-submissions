class Solution:
    def trap(self, height: List[int]) -> int:
        hh=len(height)
        leftmax=[0]*hh
        maxhh=height[0]
        for i in range(1,hh):
            maxhh=max(height[i],maxhh)
            leftmax[i]=maxhh

        minhh=0
        water=0
        for i in range(hh-1,-1,-1):
            x=min(minhh,leftmax[i])
            if x > height[i]:
                water+= x-height[i]
            
            minhh=max(minhh,height[i])
        return water