class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        l = len(nums)

        def dfs(s, sub):
            res.append(sub)
            if s == l:
                return
            for i in range(s, l):
                if i > s and nums[i] == nums[i - 1]:
                    continue
                dfs(i + 1, sub + [nums[i]])

        nums.sort()
        dfs(0, [])
        return res
