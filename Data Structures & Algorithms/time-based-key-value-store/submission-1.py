class TimeMap:

    def __init__(self):
        self.mapx=defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapx[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        sol=""
        x=self.mapx[key]
        l=0
        r=len(x)-1

        while (l<=r):
            mid=(l+r)//2

            if (x[mid][0]==timestamp):
                return x[mid][1]
            elif (x[mid][0]>timestamp):
                r=mid-1
            elif(x[mid][0]<timestamp):
                sol=x[mid][1]
                l=mid+1
        
        return sol
        
