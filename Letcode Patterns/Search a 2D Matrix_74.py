class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        lo = 0
        hi = r * c
        while lo < hi:
            m = (lo + hi) // 2
            i = m // c
            j = m % c
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                lo = m + 1
            else:
                hi = m
        return False
