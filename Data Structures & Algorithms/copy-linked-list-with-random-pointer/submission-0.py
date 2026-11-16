"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        maps={None:None}
        temp=head

        while temp:
            newnode=Node(x=temp.val)
            maps[temp]=newnode
            temp=temp.next

        temp=head

        while temp:
            maps[temp].random=maps[temp.random]
            maps[temp].next=maps[temp.next]
            
            temp=temp.next
        return maps[head]