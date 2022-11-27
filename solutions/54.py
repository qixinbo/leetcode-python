class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []
        seen = set()
        def dfs(i, j, direction):
            seen.add((i, j))
            res.append(matrix[i][j])
            if direction == 'right':
                if j+1 < n and (i, j+1) not in seen:
                    dfs(i, j+1, 'right')
                elif i+1 < m and (i+1, j) not in seen:
                    dfs(i+1, j, 'down')
            if direction == 'down':
                if i+1 < m and (i+1, j) not in seen:
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

        return res
