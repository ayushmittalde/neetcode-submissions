class Solution:
    from collections import deque
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS =len(grid)
        COLS=len(grid[0])
        queue=deque()
        INF=2147483647
        dis=0
        
        def search(r,c):
            nonlocal dis
            if r<0 or c<0 or r==ROWS or c==COLS or grid[r][c]==-1 or grid[r][c]==0:
                return 
            if grid[r][c]==INF:
                grid[r][c]=dis+1
                queue.append((r,c))

        for r in range(ROWS):
            for c in range (COLS):
                if grid[r][c]==0:
                    queue.append((r,c))
        
        while queue :
            r,c=queue.popleft()
            dis=grid[r][c]
            search(r+1,c)
            search(r-1,c)
            search(r,c+1)
            search(r,c-1)

