class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        res = []

        def backtrack(s, sub, r):
            if s == l:
                res.append(sub)
                return
            for i in nums:
                if not i in r:
                    r.add(i)
                    backtrack(s + 1, sub + [i], r)
                    r.remove(i)

        backtrack(0, [], set())
        return res
