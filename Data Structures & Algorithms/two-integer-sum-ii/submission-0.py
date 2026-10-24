class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f=0
        l=len(numbers)-1

        while (f<l):
            sumx=numbers[f]+numbers[l]
            if (sumx==target):
                return [f+1, l+1]
            elif (sumx>target):
                l-=1
            elif (sumx<target):
                f+=1
        
    
