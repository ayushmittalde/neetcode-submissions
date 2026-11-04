class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        time=[]
        for i in range(len(position)):
            time.append([position[i],(target-position[i])/speed[i]])
        
        time.sort()
        fleet=0
        stack=[]

        for i in range(len(time)-1,-1,-1):

            while len(stack) and time[i][1]>stack[-1]:
                stack.pop()
            
            if stack:
                continue
            else :
                stack.append(time[i][1])
                fleet+=1
            
        
        return fleet
        

        