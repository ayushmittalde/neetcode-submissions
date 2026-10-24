# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        sol=0

        def height(root):
            nonlocal sol
            if not root:
                return 0
            x=height(root.left)
            y=height(root.right)
            sol=max(sol,x+y)
            return max(x,y)+1
        x=height(root)
        return sol