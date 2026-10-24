# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        sol=[]

        def store(root):
            if not root:
                sol.append("N")
                return
            
            sol.append(str(root.val))
            store(root.left)
            store(root.right)
        
        store(root)
        x=",".join(sol)
        return x

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        vals=data.split(",")
        print(vals)
        self.i=0
        def build(vals):
            if vals[self.i]=='N':
                self.i+=1
                return None
            
            root=TreeNode(int(vals[self.i]))
            self.i+=1
            root.left=build(vals)
            root.right=build(vals)

            return root
        
        return build(vals)
