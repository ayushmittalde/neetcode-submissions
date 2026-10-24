class Node:
    def __init__(self):
        self.val=0
        self.key=None
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.count=0

        self.left=Node()
        self.right=Node()
        self.left.next=self.right
        self.right.prev=self.left
        
        self.cache={}
    
    def delete(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def insert(self,node):
        temp=self.right.prev
        temp.next=node
        node.prev=temp
        node.next=self.right
        self.right.prev=node

    def move(self,node):
        self.delete(node)
        self.insert(node)

    def get(self, key: int) -> int:
        if key in self.cache:
            self.move(self.cache[key])
            return self.cache[key].val
        else :
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            print(key,"x1")
            self.move(self.cache[key])
            self.cache[key].val=value

        elif self.count <self.capacity:
            print(key,"x2")
            x=Node()
            x.val=value
            x.key=key
            self.cache[key]=x
            self.insert(x)
            self.count+=1
            print(self.count,self.capacity)

        elif self.count ==self.capacity:
            print(key,"x3")
            lru=self.left.next
            self.delete(self.left.next)
            del self.cache[lru.key]
            x=Node()
            x.val=value
            x.key=key
            self.cache[key]=x
            self.insert(x)
            

        
