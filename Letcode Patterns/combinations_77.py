class Solution:
    def combine(self, n: int, k: int) -> [[int]]:
        if n == 0 or k == 0:
            return [[]]
        res = []

        def backtrack(s, c):
            if s - 1 == k:
                res.append(c)
                return

            i = 0 if not c else c[-1]
            for j in range(i + 1, n + 1):
                backtrack(s + 1, c + [j])

        backtrack(1, [])
        return res
