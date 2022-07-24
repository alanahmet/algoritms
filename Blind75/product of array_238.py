class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        res = [1]
        product = 1
        for i in range(1, len(nums)):
            product *= nums[i - 1]
            res.append(product)
        product = 1
        for i in range(len(nums) - 1, 0, -1):
            res[i] = res[i] * product
            product *= nums[i]
        res[0] = res[0] * product
        return res


sol = Solution()
Sol = sol.productExceptSelf([1, 2, 3])
