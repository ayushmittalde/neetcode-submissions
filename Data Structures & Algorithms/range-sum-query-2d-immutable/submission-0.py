class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row_len=len(matrix[0])
        col_len=len(matrix)

        prefix=0
        self.store=[[0]*(row_len+1) for _ in range (col_len+1)]

        for r in range(col_len):
            prefix=0
            for c in range (row_len):
                prefix+=matrix[r][c]
                self.store[r+1][c+1]=prefix+self.store[r][c+1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        row1 , col1 , row2, col2 = row1+1 , col1+1 , row2+1, col2+1 
        sum=self.store[row2][col2]-self.store[row1-1][col2]-self.store[row2][col1-1]+self.store[row1-1][col1-1]
        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)