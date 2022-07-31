class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        r, c = len(matrix) - 1, 0
        print(len(matrix[0]) - 1)
        while r >= 0 and c < len(matrix[0]):
            print(r, c)
            if matrix[r][c] == target:
                return True
            if matrix[r][c] < target:
                c += 1
            else:
                r -= 1
        return False


print(Solution().searchMatrix(
    [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20))
