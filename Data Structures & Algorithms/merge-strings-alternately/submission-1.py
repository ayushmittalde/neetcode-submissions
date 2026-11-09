class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=[]
        i=0
        r=0

        while (i<len(word1) and r<len(word2)):
            result.append(word1[i])
            result.append(word2[r])
            i+=1
            r+=1
        
        result.extend(word1[i:])
        result.extend(word2[r:])

        return "".join(result)