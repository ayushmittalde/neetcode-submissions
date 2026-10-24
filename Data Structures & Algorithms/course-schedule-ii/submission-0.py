class Solution:
    def findOrder(self, numCourses: int, prereq: List[List[int]]) -> List[int]:
        stack=[]
        cycle=[]

        vert=list()

        for i in range(numCourses):
            vert.append([])
        
        for idx,val in prereq:
            vert[idx].append(val)
        visit=set()

        def dfs(i):
            if i in cycle:
                return False
            if i in visit:
                return True
                            
            visit.add(i)
            cycle.append(i)

            for edge in vert[i]:
                if dfs(edge)==False:
                    return False
            
            cycle.pop()
            
            stack.append(i)

            return True


        for i in range(numCourses):
            if i not in visit:
                if dfs(i)==False:
                    return []
        
        return stack