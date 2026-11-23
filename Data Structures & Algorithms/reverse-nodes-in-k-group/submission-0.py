# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse (self,head):
        prev=None
        curr=head
        save=None
        while(curr):
            save=curr.next
            curr.next=prev
            prev=curr
            curr=save
        
        head,tail=prev,head
        return head,tail


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        bisect=[]
        bisect.append(head)
        
        curr=head
        count=0

        while curr:
            count +=1
            
            if count ==k:
                save=curr.next
                bisect.append(save)
                curr.next=None 
                count=0
                curr=save
                continue

            curr=curr.next
            

        
        last=None
        if count !=k:
            last=bisect.pop()

        masterhead,mastertail=self.reverse(bisect[0])
        
        for i in range(1,len(bisect)):
            h,t=self.reverse(bisect[i])
            mastertail.next=h
            mastertail=t

        mastertail.next=last

        return masterhead

        
        

