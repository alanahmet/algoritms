class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        res = []

        def dfs(o, c, stack):
            if o == c and o == n:
                res.append(stack)
                return
            if o + c < 2 * n and o >= c:
                dfs(o + 1, c, stack + "(")
                dfs(o, c + 1, stack + ")")

        dfs(0, 0, "")
        return res
