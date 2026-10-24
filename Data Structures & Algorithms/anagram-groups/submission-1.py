class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap =defaultdict(list)
        
        for index , val in enumerate(strs):
            temp = "".join(sorted(val))
            wordMap[temp].append(val)

        return wordMap.values()
        
        