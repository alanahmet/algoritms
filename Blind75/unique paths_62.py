class Solution(object):
    def uniquePaths(self, r, c):
        board = [[0 for x in range(c + 1)] for j in range(r + 1)]
        for i in range(c + 1):
            board[r - 1][i] = 1
        for i in range(r - 1, -1, -1):
            for j in range(c - 1, -1, -1):
                board[i][j] = board[i][j + 1] + board[i + 1][j]

        return board[0][0]


print(Solution().uniquePaths(3, 7))

"""     
        def uniquePaths(self, m: int, n: int) -> int:
        total = 0
        max_num = max(m,n)
        m = min(m,n)
        n = max_num
        if n > 2 and m > 1:
            total += (n - 2) * (m - 1) * 2
            total += (n - 2)
            total += (m - 2)
            total += (m - 2) * 2
        if n == 2 and m == 2:
            return 2
        return total
        
        def uniquePaths(self, m: int, n: int) -> int:  #Work for small values
        self.paths = 0

        def helper(r, c):
            if r > m or c > n:
                return
            if r == m and c == n:
                self.paths += 1
                return
            helper(r + 1, c)
            helper(r, c + 1)

        helper(1, 1)
        return self.paths"""
