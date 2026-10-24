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
        ListNode* sh=nullptr;
        ListNode* shc=nullptr;

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

        //Base case : to set the head
        if (h1->val <= h2->val)
        {
            sh = h1;
            h1 =h1->next;
        }
        else if (h1->val > h2->val)
        {
            sh = h2;
            h2=h2->next;
        } 

        shc=sh;

        do
        {

        if (h1==nullptr && h2==nullptr)
        {
            return sh ;
        }
        
        if (h1==nullptr)
        {
            shc->next=h2;
            return sh;
        }
        
        if (h2 == nullptr)
        {
            shc->next=h1;
            return sh;
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

        }while (1); //
         
        
    }
};
