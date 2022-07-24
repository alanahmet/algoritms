class Solution:
    def combinationSum(self, candidates: [int], target: int):
        res = []

        def bt(rest, stack, start):
            if rest == 0:
                res.append(stack)
                return
            for i in range(start, len(candidates)):
                if rest - candidates[i] >= 0:
                    bt(rest - candidates[i], stack + [candidates[i]], i)

        for i in range(0, len(candidates)):
            if target - candidates[i] >= 0:
                bt(target - candidates[i], [candidates[i]], i)
        return res
