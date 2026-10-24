class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x=defaultdict(int)
        arr=[]
        for num in nums:
            x[num]+=1

        for num , freq in x.items():
            arr.append([freq,num])
        
        arr.sort()

        result=[]

        for i in range(k):
            result.append(arr.pop()[1])
        
        return result

