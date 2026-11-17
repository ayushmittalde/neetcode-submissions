# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy=ListNode(0,head)
        endleft=dummy
        headleft=head

        i=1
        while i<left:
            endleft=headleft
            headleft=headleft.next
            i+=1
        

        i=left
        prev=None
        save=None
        temp=headleft

        while i<=right:
            save=temp.next
            temp.next=prev
            prev=temp
            temp=save
            i+=1
        
        headleft.next=temp
        endleft.next=prev

        return dummy.next


