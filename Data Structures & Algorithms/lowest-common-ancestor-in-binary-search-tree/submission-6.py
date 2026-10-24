# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def search(root,val,x):
            if root.val==val:
                x.append(root)
            elif val<root.val:
                search(root.left,val,x)
                x.append(root)
            elif val>root.val:
                search(root.right,val,x)
                x.append(root)
            
        x=[]
        y=[]

        search(root,p.val,x)
        search(root,q.val,y)

        for i in x:
            if i in y :
                return i

 