class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row_flag, column_flag = [False] * m, [False] * n 
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_flag[i] = column_flag[j] = True
        for i in range(m):
            for j in range(n):
                if row_flag[i] or column_flag[j]:
                    matrix[i][j] = 0
