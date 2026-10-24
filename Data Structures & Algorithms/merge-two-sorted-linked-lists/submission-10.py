# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        sol=ListNode(-101,None)
        curr=sol
        head1=list1
        head2=list2
        while (head1 and head2):
            if (head1.val==head2.val):
                curr.next=ListNode(head1.val,None)
                curr=curr.next
                curr.next=ListNode(head2.val,None)
                curr=curr.next
                head1=head1.next
                head2=head2.next
            elif (head1.val>head2.val):
                curr.next=ListNode(head2.val,None)
                curr=curr.next
                head2=head2.next
            else:
                curr.next=ListNode(head1.val,None)
                curr=curr.next
                head1=head1.next
        

            curr.next= head1 or head2

        return sol.next




        
        