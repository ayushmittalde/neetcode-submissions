# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=fast=head

        while (fast and fast.next):
            slow=slow.next
            fast=fast.next.next
   
        #reverse 
        prev=None
        curr=slow.next
        save=None

        slow.next=None
        # the second loop runs on the second half of the linked list because it is always smaller than the first half
        while curr: 
            save=curr.next
            curr.next=prev
            prev=curr
            curr=save
        
        save=None
        head1=head
        head2=prev
        while head2:
            save=head1.next
            head1.next=head2
            head2=head2.next
            head1.next.next=save
            head1=head1.next.next

        

