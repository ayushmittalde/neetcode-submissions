def palindrome (s):
    return s==s[::-1]

class Solution:
    def validPalindrome(self, s: str) -> bool:

        if palindrome(s):
            return True
            
        i=0
        r=len(s)-1
        while (i<r):
            
            if s[i]!=s[r]:
                cand1=s[i:r]
                cand2=s[i+1:r+1]
                return palindrome(cand1) or palindrome(cand2)
            i+=1
            r-=1
        
        return True