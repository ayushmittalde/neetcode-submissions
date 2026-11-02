class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[]
        score=0

        for i in operations:
            if i == '+':
                temp=record[-1]+record[-2]
                record.append(temp)
                score+=temp
            elif i == 'D':
                temp=record[-1]*2
                record.append(temp)
                score+=(temp)
            elif i == 'C':
                x=record.pop()
                score-=x
            else:
                record.append(int(i))
                score+=int(i)
                
        return score