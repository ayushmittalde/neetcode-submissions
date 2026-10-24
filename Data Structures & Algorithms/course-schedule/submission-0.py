class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

    
        adj=defaultdict(list)
        for idx, val in prerequisites:
            adj[idx].append(val)

        stack=[]
        visited=set()

    
        def dfs(idx):
            if idx in stack :
                return True
            
            visited.add(idx)
            stack.append(idx)
            for i in adj[idx]:
                if dfs(i):
                    return True 
            stack.pop()
            return False

        for idx in range(numCourses):
            if idx not in visited:
                if dfs(idx):
                    return False
        
        return True

