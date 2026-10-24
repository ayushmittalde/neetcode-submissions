# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        sol=[]
        temp=[]
        q=queue.Queue()
        if not root:
            return []
        q.put(root)
        q.put(None)

        while q.empty()!=True:
            x=q.get()

            if x==None:
                sol.append(temp.pop())
                if q.empty()!=True:
                    q.put(None)
            else:
                temp.append(x.val)
                if x.left !=None:
                    q.put(x.left)
                if x.right !=None:
                    q.put(x.right)
        return sol
        