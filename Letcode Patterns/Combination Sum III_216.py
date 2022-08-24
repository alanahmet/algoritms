class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def bc(i, stack, s_sum):
            if len(stack) == k:
                if s_sum == n: res.append(stack)
                return

            for j in range(i, 10):
                if s_sum + j <= n:
                    bc(j + 1, stack + [j], s_sum + j)
        res = []
        bc(1, [], 0)
        return res
