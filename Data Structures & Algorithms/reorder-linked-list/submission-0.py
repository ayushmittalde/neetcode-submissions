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
        print(slow.val)

        #rever the second part of list 
        curr=slow.next
        slow.next=None
        prev=None
        while (curr):
            save=curr.next
            curr.next=prev
            prev=curr
            curr=save

        head2=prev
        head1=head
        save=None
            
        while (head2):
            save=head1.next
            head1.next=head2
            head2=head2.next
            head1.next.next=save
            head1=head1.next.next

        



        


        