class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[]
        score=0
        index=-1

        for i in operations:
            if i == '+':
                temp=record[index]+record[index-1]
                record.append(temp)
                index+=1
                score+=temp
            elif i == 'D':
                temp=record[index]*2
                record.append(temp)
                index+=1
                score+=(temp)
            elif i == 'C':
                x=record.pop()
                index-=1
                score-=x
            else:
                record.append(int(i))
                index+=1
                score+=int(i)
        return score