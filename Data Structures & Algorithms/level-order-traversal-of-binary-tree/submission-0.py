# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        sol=[]
        y=queue.Queue()
        if not root:
            return []
        y.put(root)
        y.put(None)
        temp=[]
        while not y.empty():
            x=y.get()

            if x == None:
                sol.append(temp.copy())
                temp.clear()
                if y.empty()==False:
                    y.put(None)
            elif x != None:
                temp.append(x.val)
                if x.left !=None:
                    y.put(x.left)
                if x.right !=None:
                    y.put(x.right)

        return sol