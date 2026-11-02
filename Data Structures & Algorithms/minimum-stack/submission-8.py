class MinStack:

    def __init__(self):
        self.stack=[]
        self.minval=2**31
        
    def push(self, val: int) -> None:
        if val < self.minval:
            self.stack.append(2*val-self.minval)
            self.minval=val
        else:
            self.stack.append(val)
        
    def pop(self) -> None:
        x=self.stack.pop()
        if x < self.minval:
            self.minval=(2*self.minval)-x

    def top(self) -> int:
        if self.stack[-1] < self.minval:
            return self.minval
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.minval
        
