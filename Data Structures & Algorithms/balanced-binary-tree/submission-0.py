# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        sol=True
        def height(root):
            nonlocal sol
            if not root:
                return 0
            x=height(root.left)
            y=height(root.right)
            if (abs(x-y)>1):
                sol=sol&False
            else:
                sol=sol&True

            return (max(x,y)+1)
        
        height(root)
        return sol



        