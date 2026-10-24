# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        x=[root.val]
        def search(root):
            nonlocal count
            if not root :
                return 0

            if root.val >= max(x):
                count+=1

            x.append(root.val)
            search(root.left)
            search(root.right)
            x.pop()
        
        search(root)
        return count

        