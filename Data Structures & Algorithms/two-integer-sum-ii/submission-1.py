class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        l=0
        r=len(num)-1

        while(l<r):
            cand=target-num[l]
            if (cand==num[r]):
                return [l+1,r+1]
            elif(cand>num[r]):
                l+=1
            else:
                r-=1
        
