class MyQueue:

    def __init__(self):
        self.s=[]
        self.q=[]
        

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:

        if len(self.q)!=0:
            return self.q.pop()
        else:
            while (len(self.s)):
                self.q.append(self.s.pop())
            return self.q.pop()

    def peek(self) -> int:

        if len(self.q)!=0:
            return self.q[-1]
        else:
            while (len(self.s)):
                self.q.append(self.s.pop())
            return self.q[-1]

    def empty(self) -> bool:
        return (len(self.s) + len(self.q))==0 
