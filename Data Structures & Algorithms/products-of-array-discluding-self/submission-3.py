class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        if (nums.count(0)>1):
            return [0 for _ in range(length)]
            
        leftprod=[1]*length
        rightprod=1
        prod=[1]*length

        l=1
        r=length-1

        while(l<length):
            leftprod[l]=leftprod[l-1]*nums[l-1]
            l+=1

        while(r>=0):
            prod[r]=leftprod[r]*rightprod
            rightprod=rightprod*nums[r]
            r-=1

        return prod