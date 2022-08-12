class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        board = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                board[j] += board[j - 1]
        return board[-1]
