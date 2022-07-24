class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        ans = []
        l = len(nums)

        def dfs(s, sub):
            ans.append(sub)
            for i in range(s, l):
                dfs(i + 1, sub + [nums[i]])

        dfs(0, [])
        return ans
a