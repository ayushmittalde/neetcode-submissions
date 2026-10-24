class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=s.replace(" ","")
        f =0
        l=len(s)-1
        
        while (f<l):
            while (self.check(s[f])==False and f<l):
                f+=1
            while (self.check(s[l])==False and f<l):
                l-=1
            
            if (s[f]==s[l]):
                f+=1
                l-=1
            else :
                return False

        return True

    def check(self, c):
        if (ord('a')<=ord(c)<=ord('z')):
            return True
        elif (ord('A')<=ord(c)<=ord('Z')):
            return True
        elif (ord('0')<=ord(c)<=ord('9')):
            return True
        else:
            return False