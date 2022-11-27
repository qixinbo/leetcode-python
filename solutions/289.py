class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        flag = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                count = 0
                for x, y in ((i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)):
                    if 0 <= x < m and 0 <= y < n and board[x][y] == 1:
                        count += 1
                if (board[i][j] and 2 <= count <=3) or (not board[i][j] and count==3):
                    flag[i][j] = 1
        for i in range(m):
            for j in range(n):
                board[i][j] = 1 if flag[i][j] else 0
