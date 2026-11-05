class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result=[]

        for i in words:
            for x in words:
                if i==x:
                    continue

                elif i in x:
                    result.append(i)
                    break
        
        return result
        