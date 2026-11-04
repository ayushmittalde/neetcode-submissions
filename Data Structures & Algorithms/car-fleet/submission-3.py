class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        time=[-1]*target
        for i in range(len(position)):
            time[position[i]]=(target-position[i])/speed[i]
        
        fleet=0
        maxele=-1

        for i in range(target-1,-1,-1):
            if time[i]>maxele:
                fleet+=1
                maxele=time[i]
        
        return fleet