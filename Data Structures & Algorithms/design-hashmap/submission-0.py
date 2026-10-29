class node():

    def __init__(self,key:int,value:int):
        self.next=None
        self.key=key
        self.value=value

class MyHashMap:

    def __init__(self):
        self.store=[node(None,None) for _ in range(10007)]
        

    def put(self, key: int, value: int) -> None:
        hash=key%10007
        curr=self.store[hash]
        
        while (curr.next):
            if (curr.next.key==key):
                curr.next.value=value
                return None
            curr=curr.next
        
        curr.next=node(key,value)



        return None

    def get(self, key: int) -> int:
        hash=key%10007
        curr=self.store[hash]
        
        while (curr.next):
            if (curr.next.key==key):
                return curr.next.value
            curr=curr.next

        return -1
        

    def remove(self, key: int) -> None:
        hash=key%10007
        curr=self.store[hash]
        
        while (curr.next):
            if (curr.next.key==key):
                curr.next=curr.next.next
                return None
            curr=curr.next
        
        return None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)