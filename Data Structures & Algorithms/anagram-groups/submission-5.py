class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=defaultdict(list)

        for name in strs:
            count=[0]*26
            
            for i in name:
                count[ord(i)-ord("a")]+=1

            group[tuple(count)].append(name)
            
        return list(group.values())