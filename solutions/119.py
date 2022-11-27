class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        total = [[1]]
        for _ in range(rowIndex):
            total.append([1]+[a+b for a, b in zip(total[-1], total[-1][1:])] + [1])
        return total[rowIndex]
