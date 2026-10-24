class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setx=set()
        l=r=0
        x=len(s)
        sol=0
        while(r<x):
            if s[r] not in setx:
                setx.add(s[r])
                r+=1
                sol=max(sol,len(setx))
            elif(s[r] in setx):
                while (s[r] in setx and l<r):
                    setx.remove(s[l])
                    l+=1
        return sol