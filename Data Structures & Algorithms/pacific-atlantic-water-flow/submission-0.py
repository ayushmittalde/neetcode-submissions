class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS=len(grid)
        COLS=len(grid[0])
        from collections import deque
        mapx=defaultdict(list)
        pac=deque()
        atl=deque()
        sol=[]

        for r in range(ROWS):
            for c in range(COLS):
                mapx[(r,c)]=[None,None]

        for c in range(COLS):
            mapx[(0,c)]=[1,None]
            pac.append((0,c))
            mapx[(ROWS-1,c)]=[None,1]
            atl.append((ROWS-1,c))
            
        for r in range(ROWS):
            mapx[(r,0)][0]=1
            pac.append((r,0))
            mapx[(r,COLS-1)][1]=1
            atl.append((r,COLS-1))
        
        rx=0
        cx=0
        def runpac(r,c):
            nonlocal rx , cx
            if r<0 or c<0 or r==ROWS or c==COLS:
                return
            if mapx[(r,c)][0]!=1:
                if grid[r][c]>=grid[rx][cx]:
                    mapx[(r,c)][0]=1
                    pac.append((r,c))
                else:
                    mapx[(r,c)][0]=None
            return

        def runatl(r,c):
            nonlocal rx , cx,sol,ROWS,COLS
            if r<0 or c<0 or r==ROWS or c==COLS:
                return
            elif mapx[(r,c)][1]!=1:
                if grid[r][c]>=grid[rx][cx]:
                    mapx[(r,c)][1]=1
                    atl.append((r,c))
                    if mapx[(r,c)]==[1,1]:
                        sol.append([r,c])
                else:
                    mapx[(r,c)][1]=None
            return

        while pac:
            rx,cx = pac.popleft()
            runpac(rx+1,cx)
            runpac(rx-1,cx)
            runpac(rx,cx+1)
            runpac(rx,cx-1)

        while atl:
            rx,cx = atl.popleft()
            if mapx[(rx,cx)]==[1,1] and [rx,cx] not in sol:
                sol.append([rx,cx])
            runatl(rx+1,cx)
            runatl(rx-1,cx)
            runatl(rx,cx+1)
            runatl(rx,cx-1)

        return sol
        


        
