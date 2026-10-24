/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {

        ListNode* h1 = list1;
        ListNode* h2 = list2; 
        ListNode dummy ;
        dummy.val=0;
        dummy.next=nullptr;
        ListNode* shc= &dummy;

        if (list1==nullptr && list2==nullptr)
        {
            return nullptr;
        }
        else if (list1==nullptr)
        {
            return list2;
        }
        else if (list2 == nullptr)
        {
            return list1;
        }

        do
        {

        if (h1==nullptr && h2==nullptr)
        {
            return dummy.next ;
        }
        
        if (h1==nullptr)
        {
            shc->next=h2;
            return dummy.next;
        }
        
        if (h2 == nullptr)
        {
            shc->next=h1;
            return dummy.next;
        }

        
        if (h1->val < h2->val)
        {
            shc->next=h1;
            h1=h1->next;
            shc=shc->next;
        }
        else if (h1->val == h2->val)
        {
            shc->next=h1;
            h1=h1->next;
            shc=shc->next;
            shc->next=h2;
            h2=h2->next;
            shc=shc->next;
        }

        else if (h1->val > h2->val)
        {
            shc->next=h2;
            h2=h2->next;
            shc=shc->next;
        }

        }while (1);

         
        
    }
};
