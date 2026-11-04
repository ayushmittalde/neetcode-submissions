class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        time=[]
        for i in range(len(position)):
            time.append([position[i],(target-position[i])/speed[i]])
        
        time.sort()
        fleet=0
        maxele=-1

        for i in range(len(time)-1,-1,-1):
            if time[i][1]>maxele:
                fleet+=1
                maxele=time[i][1]
        
        return fleet