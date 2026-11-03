class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[0]*len(temperatures)

        for i in range(len(temperatures)-1,-1,-1):

            if len(stack)==0:
                result[i]=0
                stack.append([temperatures[i],i])
            else : 
                while len(stack):
                
                    if temperatures[i]>=stack[-1][0]:
                        stack.pop()
                        if len(stack)==0:
                            result[i]=0
                            stack.append([temperatures[i],i])
                            break
                    else:
                        result[i]=stack[-1][1]-i
                        stack.append([temperatures[i],i])
                        break
                
        return result