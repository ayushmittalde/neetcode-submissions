class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap ={} # sort : index
        
        for index , val in enumerate(strs):
            temp = "".join(sorted(val))
            if temp in wordMap:
                wordMap[temp].append(val)
            else :
                wordMap[temp]=[val]

        solution =[]

        for key in wordMap:
            solution.append(wordMap[key])

        return solution
        
        