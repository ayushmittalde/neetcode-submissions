class MinStack:

    def __init__(self):
        self.stack=[]
        self.minval=2**31
        

    def push(self, val: int) -> None:
        self.minval=min(self.minval,val)
        self.stack.append([val,self.minval])
        

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.minval=self.stack[-1][1]
        else:
            self.minval=2**31
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
