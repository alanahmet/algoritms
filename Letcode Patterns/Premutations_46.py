class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, visited, l = [], [False] * len(nums), len(nums)

        def bc(part):
            if len(part) == l:
                res.append(part)
                return
            for i, v in enumerate(nums):
                if not visited[i]:
                    visited[i] = True
                    bc(part + [v])
                    visited[i] = False

        bc([])
        return res
