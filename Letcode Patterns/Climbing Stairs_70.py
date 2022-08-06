class Solution:
    def climbStairs(self, n: int) -> int:
        p1, p2 = 1, 1
        for _ in range(2, n + 1):
            temp = p1 + p2
            p1, p2 = p2, temp
        return p2
