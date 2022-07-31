class Solution:
    def missingNumber(self, nums: [int]) -> int:
        ans = len(nums)

        for i, num in enumerate(nums):
            ans ^= i ^ num
print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))