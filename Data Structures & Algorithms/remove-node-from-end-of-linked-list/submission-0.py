# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head :
            return head
        size=0
        curr=head
        while (curr):
            size+=1
            curr=curr.next

        curr=head
        jump=size-n
        i=1
        if (jump==0):
            return head.next

        while(i!=jump):
            curr=curr.next
            i+=1
        
        curr.next=curr.next.next

        return head


        