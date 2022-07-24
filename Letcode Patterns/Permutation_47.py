class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        res = []

        def backtrack(sub, rem):
            if len(sub) == l:
                res.append(sub)
                return
            for i in range(len(rem)):
                if i > 0 and rem[i] != rem[i - 1]:
                    backtrack(sub + [rem[i]], rem[:i] + rem[i + 1:])
                if i == 0:
                    backtrack(sub + [rem[i]], rem[:i] + rem[i + 1:])

        nums.sort()
        backtrack([], nums)
        return res
