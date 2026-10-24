# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def check(sub,root):
            if sub == root ==None:
                return True
            elif sub and not root:
                return False
            elif not sub and root:
                return False
            
            if (check(sub.left,root.left) and sub.val==root.val and check(sub.right,root.right) ):
                return True
            else:
                return False

        nodes=[]
        
        def search(x,root,nodes):

            if not root:
                return None
            if root.val==x:
                nodes.append(root)

            search(x,root.left,nodes)
            search(x,root.right,nodes)

        search(subRoot.val,root,nodes)
        for x in nodes:
            if check(subRoot,x):
                return True

        return False
            

        
