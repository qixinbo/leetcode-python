from typing import List 

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        print(matrix)

s = Solution()
s.generateMatrix(6)

