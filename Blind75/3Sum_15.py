class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        res = []
        nums.sort()
        print(nums)
        for i, a in enumerate(nums):
            if i > 0 and a == [i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                treesum = a + nums[l] + nums[r]
                if treesum > 0:
                    r -= 1
                elif treesum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res

""" 
        res = []
        nums = list(set(nums))
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                print(f"i. {nums[i]} j:{nums[j]}")
                tsum = nums[i] + nums[j]
                if -tsum in nums[j:]:
                    res.append([nums[i], nums[j], -tsum])
        return res"""
Sol = Solution()
sol = Sol.threeSum([-1, 0, 1, 2, -1, -4])
print(sol)
