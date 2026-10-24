# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sol=[]

        def search(root,sol,k):
            if not root:
                return None
            
            if len(sol)<k:
                search(root.left,sol,k)
            if len(sol)<k:
                sol.append(root.val)
            if len(sol)<k:
                search(root.right,sol,k)
        
        search(root,sol,k)
        return sol.pop()