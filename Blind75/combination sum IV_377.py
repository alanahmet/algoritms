"""My dummy version (not working for large possibilities)
class Solution:
    def combinationSum4(self, nums: [int], target: int) -> int:
        array = []
        self.possible = 0

        def combination(nums: [int], arr: []):
            arr_sum = sum(arr)
            if arr_sum == target:
                self.possible += 1
                return
            if arr_sum > target:
                return
            for i in nums:
                arr.append(i)
                combination(nums,arr)
                arr.pop()
        combination(nums,array)
        return self.possible"""

class Solution:
    def combinationSum4(self, nums: [int], target: int) -> int:
        dp = {0: 1}
        for total in range(1, target + 1):
           dp[total] = 0
           for i in nums:
               dp[total] += dp.get(total - i,0)
        print(dp)
        print("\n")

        return dp[target]

print(Solution().combinationSum4([3,4,1],32))