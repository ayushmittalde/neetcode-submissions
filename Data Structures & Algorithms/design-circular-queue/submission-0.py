class Node:
    def __init__(self,val,next):
        self.val=val
        self.next=next

class MyCircularQueue:

    def __init__(self, k: int):
        self.head=Node(0,None)
        self.tail=Node(0,None)
        self.count=0
        self.limit=k
        self.head.next=self.tail


    def enQueue(self, value: int) -> bool:
        
        if self.count==self.limit:
            return False
        
        temp=Node(value,self.head.next)
        self.head.next=temp
        self.count+=1

        return True

    def deQueue(self) -> bool:
        
        if self.count ==0:
            return False
        
        prev=self.head
        curr=self.head.next

        while curr.next !=self.tail :
            prev=curr
            curr=curr.next
        
        prev.next=self.tail
        self.count-=1
        return True


    def Rear(self) -> int:
        if self.count ==0:
            return -1
        
        return self.head.next.val


    def Front(self) -> int:
        if self.count ==0:
            return -1
        
        curr=self.head.next

        while curr.next !=self.tail :
            curr=curr.next
        
        return curr.val

    def isEmpty(self) -> bool:
        if self.count ==0:
            return True
        
        return False

    def isFull(self) -> bool:
        if self.count ==self.limit:
            return True
        
        return False       


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()