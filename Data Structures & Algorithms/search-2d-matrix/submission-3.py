class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=sum(len(x) for x in matrix)-1
        row_len=len(matrix[0])
        while (l<=r):
            x=(l+r)//2
            m,n=(x//row_len),(x%row_len)

            if (matrix[m][n]==target):
                return True
            elif (matrix[m][n]<target):
                l=x+1
            else :
                r=x-1

        return False
        