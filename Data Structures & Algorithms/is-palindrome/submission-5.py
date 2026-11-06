class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        y="".join([c for c in s if c.isalnum()])

        l=0
        r=len(y)-1
        while (l<r):
            if (y[l]!=y[r]):
                return False
            l+=1
            r-=1
            
        return True
