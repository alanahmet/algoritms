class Solution:
    def rotate(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l,r = 0, len(matrix)
        while l < r:
            top, bottom = l, r
            top_left = matrix[top][l+i]

            #Bottom left
            for i in range(r - 1):
                matrix[top][l + i] = matrix[bottom - i][l]


