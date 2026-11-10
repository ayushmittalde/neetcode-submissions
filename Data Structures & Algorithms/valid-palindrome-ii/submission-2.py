class Solution:
    def validPalindrome(self, s: str) -> bool:

        if s==s[::-1]:
            return True

        i=0
        r=len(s)-1
        while (i<r):
            
            if s[i]!=s[r]:
                cand1=s[i:r]
                cand2=s[i+1:r+1]
                return cand1==cand1[::-1] or cand2==cand2[::-1]
            i+=1
            r-=1
        
        return True