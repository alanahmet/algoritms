class Solution:
    def partition(self, s):
        res = []

        def dfs(r, ps):
            if not r:
                res.append(ps)
                return
            for i in range(1, len(r) + 1):
                c = r[:i]
                if c == c[::-1]:
                    dfs(r[i:], ps + [r[:i]])

        dfs(s, [])
        return res


print(Solution().partition("assdd"))

"""
    def allpolindrom(self, s: str) -> [[str]]:
        res = []
        ss = {}
        for i in s: ss[i] = 1 if not ss.get(i) else ss[i] + 1
        def bc(ps, rs: dict):  # polindrome string, remaning set
            if ps:
                res.append(ps + ps[::-1])
            for k, v in rs.items():
                if v > 1:
                    rs[k] -= 2
                    bc(ps + k, rs)
                    rs[k] += 2
                if v == 1 and ps:
                    res.append(ps + k + ps[::-1])

        bc("", ss)
        return res
"""
