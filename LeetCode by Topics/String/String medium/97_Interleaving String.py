class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        r, c = len(s1), len(s2)

        if r + c != len(s3):
            return False

        dp = [[False] * (c + 1) for _ in range(r + 1)]
        dp[r][c] = True

        for i in range(r, -1, -1):
            for j in range(c, -1, -1):
                if i < r and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < c and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True

        return dp[0][0]