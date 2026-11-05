class Solution:
    def stringMatching(self, wordx: List[str]) -> List[str]:
        words=sorted(wordx,key=len)
        result=[]

        for i in range(len(words)):
            for x in words[i+1:]:
                if words[i] in x:
                    result.append(words[i])
                    break
        
        return result