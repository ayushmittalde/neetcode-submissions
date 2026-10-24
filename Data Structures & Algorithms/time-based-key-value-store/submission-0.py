class TimeMap:

    def __init__(self):
        self.mapx=defaultdict(dict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapx[key][timestamp]=value
        

    def get(self, key: str, timestamp: int) -> str:
        sol=""
        while (sol=="" and timestamp>0):
            sol = self.mapx[key].get(timestamp,"")
            timestamp-=1
        
        return sol
        
