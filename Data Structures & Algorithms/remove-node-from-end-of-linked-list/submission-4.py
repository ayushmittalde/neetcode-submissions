# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast=head
        for i in range (1,n):
            fast=fast.next
        
        prev=None
        slow=head
        while fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next
        
        if prev:
            prev.next=slow.next
        else:
            head=slow.next
            
        return head
