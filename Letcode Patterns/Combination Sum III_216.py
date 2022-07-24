class Solution:
    def combinationSum3(self, k: int, n: int) -> [[int]]:
        res = []

        def dfs(s, l, stack, start):
            if s == n and l == k:
                res.append(stack)
                return
            for i in range(start, 10):
                if s + i <= n:
                    dfs(s + i, l + 1, stack + [i], i + 1)

        dfs(0, 0, [], 1)
        return res
