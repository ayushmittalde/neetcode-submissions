class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        sol=0

        ROWS=len(grid)
        COLS=len(grid[0])
        visit=set()

        def dfs(r,c):
            if r <0 or c<0 or r==ROWS or c==COLS or (r,c) in visit or grid[r][c]=="0":
                return False
            
            visit.add((r,c))
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)

            return True

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit:
                    if dfs(r,c):
                        sol+=1
        return sol

        