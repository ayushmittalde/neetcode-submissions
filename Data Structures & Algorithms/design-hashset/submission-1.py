class node:
    def __init__(self,key:int):
        self.key=key
        self.next=None

class MyHashSet:


    def __init__(self):
        self.store= [node(None) for _ in range(10007)]

    def add(self, key: int) -> None:
        hash=key%10007
        curr=self.store[hash]
        
        while (curr.next!=None):
            if curr.next.key == key:
                return None
            else :
                curr=curr.next
        
        curr.next=node(key)
        
        return None
        

    def remove(self, key: int) -> None:
        hash=key%10007
        curr=self.store[hash]
        
        while (curr.next!=None):
            if curr.next.key == key:
                curr.next=curr.next.next
                return None
            else :
                curr=curr.next
        
        return None
        

    def contains(self, key: int) -> bool:
        hash=key%10007
        curr=self.store[hash]
        
        while (curr.next!=None):
            if curr.next.key == key:
                return True
            else :
                curr=curr.next
        
        return False
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)