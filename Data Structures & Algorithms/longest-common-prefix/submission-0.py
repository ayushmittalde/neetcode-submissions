class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res=""
        for i in range(len(strs[0])):
            for name in strs:
                if(len(name)==i or name[i]!=strs[0][i]):
                    return res
            
            res+=strs[0][i]

        return res
        