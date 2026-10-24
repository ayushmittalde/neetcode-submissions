class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        time=0
        x=False
        count=0
        queue=deque()
        ROWS=len(grid)
        COLS=len(grid[0])

        def run(r,c):
            nonlocal ROWS, COLS, count
            if c<0 or r<0 or c==COLS or r==ROWS or grid[r][c]==0:
                return False
            print(r,c,grid[r][c])
            if grid[r][c]==1:
                queue.append((r,c))
                grid[r][c]=2
                count-=1
                return True
            return False
        


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    queue.append((r,c))
                elif grid[r][c]==1:
                    count+=1
        if count ==0:
            return time        
        queue.append((None,None))

        while queue:
            r,c=queue.popleft()

            if r==None and len(queue)!=0:
                queue.append((None,None))
                if x:
                    time+=1
                    x=False
                continue
            elif r==None and len(queue)==0:
                if x:
                    time+=1
                    x=False
                return -1 if (count!=0) else time

            temp=any([run(r+1,c), run(r-1,c), run(r,c+1), run(r,c-1)])
            x=temp or x
            print(queue)
            temp=False


        