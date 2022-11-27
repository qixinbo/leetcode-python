class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        seen = set()
        def dfs(i, j, direction):
            seen.add((i, j))
            matrix[i][j] = len(seen)
            if direction == 'right':
                if j+1 < n and (i, j+1) not in seen:
                    dfs(i, j+1, 'right')
                elif i+1 < n and (i+1, j) not in seen:
                    dfs(i+1, j, 'down')
            if direction == 'down':
                if i+1 < n and (i+1, j) not in seen:
                    dfs(i+1, j, 'down')
                elif j-1 >=0 and (i, j-1) not in seen:
                    dfs(i, j-1, 'left')
            if direction == 'left':
                if j-1 >= 0 and (i, j-1) not in seen:
                    dfs(i, j-1, 'left')
                elif i-1 >= 0 and (i-1, j) not in seen:
                    dfs(i-1, j, 'up')
            else:
                if i-1 >= 0 and (i-1, j) not in seen:
                    dfs(i-1, j, 'up')
                elif j+1 < n and (i, j+1) not in seen:
                    dfs(i, j+1, 'right')
                    
        dfs(0, 0, 'right')
        return matrix
