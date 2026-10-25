class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}

        for i in strs:
            x="".join(sorted(i))
            if x not in group:
                group[x] =[]

            group[x].append(i)
        
        return list(group.values())