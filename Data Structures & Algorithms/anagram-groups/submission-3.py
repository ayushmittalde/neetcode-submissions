class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}

        for i in strs:
            x="".join(sorted(i))
            group.setdefault(x, []).append(i)
        
        return list(group.values())