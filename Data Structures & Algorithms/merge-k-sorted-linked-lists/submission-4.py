# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergelist(head1 , head2):

    head=ListNode()
    temp=head

    while head1 and head2:
        if head1.val<=head2.val:
            head.next=head1
            head1=head1.next
        else:
            head.next=head2
            head2=head2.next
        
        head=head.next

    if head2:
        head.next=head2
    if head1:
        head.next=head1

    return temp.next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        master=lists

        while len(master)>1:
            mergedlists=[]
            for i in range (0,len(master),2):
                head1=master[i]
                head2=master[i+1] if i+1 < len(master) else None
                mergedlists.append(mergelist(head1 , head2))
            
            master=mergedlists
        
        return master[0]

