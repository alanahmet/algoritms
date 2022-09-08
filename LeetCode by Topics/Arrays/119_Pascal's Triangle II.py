class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        res = [[1], [1, 1]]
        rowIndex += 1
        while len(res) < rowIndex:
            new = [1]
            for i in range(1, len(res[-1])):
                new.append(res[-1][i] + res[-1][i - 1])
            new.append(1)
            res.append(new)
        return res[-1]
