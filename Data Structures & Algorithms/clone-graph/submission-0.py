"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        visited=dict()

        def clone(root):
            x=Node(root.val,[])
            visited[root]=x
            
            for node in root.neighbors:
                if node in visited:
                    x.neighbors.append(visited[node])
                else:
                    clone(node)
                    x.neighbors.append(visited[node])
        
        if not node:
            return None
        else:
            clone(node)
            return visited[node]

        