# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pinord=[]
        qinord=[]

        def traverse(node,x):
            if not node :
                return None
            else:    
                x.append(traverse(node.left,x))
                x.append(node.val)
                x.append(traverse(node.right,x))
        
        traverse(p,pinord)
        traverse(q,qinord)

        if pinord==qinord:
            return True
        else :
            return False


            


        