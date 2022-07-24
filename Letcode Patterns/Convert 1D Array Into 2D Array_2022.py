class Solution(object):
    def construct2DArray(self, original, m, n):
        if m * n != len(original):
            return []
        res = []
        for i in range(m):
            res.append(original[(i) * n:(i + 1) * n])
        return res
