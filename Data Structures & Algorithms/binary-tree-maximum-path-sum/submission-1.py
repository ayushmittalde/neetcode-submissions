# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        sol =-1000000

        def search (root):
            
            nonlocal sol
            temp=-1000000

            if not root:
                return 0
            
            x=search(root.left)
            y=search(root.right)
            sol=max(sol,x+y+root.val,x+root.val,y+root.val,root.val)

            return max(x+root.val,y+root.val,root.val)
        
        search(root)
    
        return sol



        