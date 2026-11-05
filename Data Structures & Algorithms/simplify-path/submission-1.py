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
                case _ : 
                    stack.append(x)

        return "/"+ "/".join(stack)