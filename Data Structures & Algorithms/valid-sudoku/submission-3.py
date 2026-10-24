class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x= defaultdict(int)

        for row in board:
            x=defaultdict(int)
            for val in row:
                if (val == '.'):
                    continue
                elif (x[val]==0):
                    x[val]+=1
                else: 
                    return False

        for col in range(len(board)):
            x= defaultdict(int)
            for row in board:
                x[row[col]]+=1
                
            del x['.']

            for x in x.values():
                if x>1:
                    return False

        index=[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

        for i in range (9):
            row_shift=int(i/3)*3
            col_shift=(i%3)*3
            count={}
            for x,y in index:
                if board[x+row_shift][y+col_shift] == '.':
                    continue
                elif board[x+row_shift][y+col_shift] in count:
                    return False
                else :
                    count[board[x+row_shift][y+col_shift]]=1

        return True

        