class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        string=path.split("/")

        for x in string:
            match x:
                case '' | '.': 
                    continue
                case '..':
                    if len(stack):
                        stack.pop()
                        stack.pop()
                case _ : 
                    stack.append("/")
                    stack.append(x)
        ans = "".join(stack)
        if ans : 
            return ans
        else :
            return "/"