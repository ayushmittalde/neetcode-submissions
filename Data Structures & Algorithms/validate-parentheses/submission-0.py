class Solution:
    def isValid(self, s: str) -> bool:
        x=[]
        maps={}
        maps[')']='('
        maps['}']='{'
        maps[']']='['

        for brack in s:
            if brack in ['(','[','{']:
                x.append(brack)
            else :
                if len(x)==0 or x.pop()!=maps[brack]:
                    return False
        
        return len(x)==0
                
        