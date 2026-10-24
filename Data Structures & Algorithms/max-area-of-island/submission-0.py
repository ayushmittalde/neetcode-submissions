class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        sol=0
        visit=set()

        rows=len(grid)
        cols=len(grid[0])
    
        def dfs(x,y,temp):
            if x>=rows or y >=cols or x<0 or y<0 or (x,y) in visit or grid[x][y]==0:
                return temp
            
            visit.add((x,y))
            temp+=1

            temp=dfs(x+1,y,temp)
            temp=dfs(x,y+1,temp)
            temp=dfs(x-1,y,temp)
            temp=dfs(x,y-1,temp)

            return temp
        

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit:
                    sol=max(dfs(r,c,0),sol)


        return sol
        