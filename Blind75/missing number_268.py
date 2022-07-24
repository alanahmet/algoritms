class Solution(object):
    def missingNumber(self, nums):
        smaller = nums[0]
        larger = nums[0]
        sum = 0
        for i in nums:
            sum += i
            smaller = min(smaller, i)
            larger = max(larger, i)
        expected_sum = ((larger + smaller) * (larger - smaller + 1)) / 2
        missing = int(expected_sum - sum)
        return missing if missing is not 0 else larger + 1

print(Solution().missingNumber([0,1]))