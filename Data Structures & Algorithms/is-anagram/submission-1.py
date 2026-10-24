class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s)==len(t)):
            ss=sorted(s)
            tt=sorted(t)
            if ss==tt :
                return True
            else :
                return False

        else :
            return False
        