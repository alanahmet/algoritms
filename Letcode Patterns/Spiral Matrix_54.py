class Solution:
    def spiralOrder(self, matrix):
        r, c = len(matrix), len(matrix[0])
        r1, r2, c1, c2 = 0, r - 1, 0, c - 1
        res = [0 for _ in range(r * c)]
        index = 0
        while index < r * c:
            # top row
            j = c1
            while j <= c2 and index < r * c:
                res[index] = matrix[r1][j]
                index += 1
                j += 1
            # right col
            i = r1 + 1
            while i <= r2 - 1 and index < r * c:
                res[index] = matrix[i][c2]
                index += 1
                i += 1
            # bottom row
            j = c2
            while j >= c1 and index < r * c:
                res[index] = matrix[r2][j]
                index += 1
                j -= 1
            # left col
            i = r2 - 1
            while i >= r1 + 1 and index < r * c:
                res[index] = matrix[i][c1]
                index += 1
                i -= 1
            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1
        return res
