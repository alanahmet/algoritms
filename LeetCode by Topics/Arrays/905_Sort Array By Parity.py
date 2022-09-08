class Solution:
    def sortArrayByParity(self, nums: [int]) -> [int]:
        return sorted(nums, key=lambda x: x % 2 == 1)
#         e = 0
#         for i in range(len(nums)):
#             while 0 <= e < len(nums) and nums[e] % 2 != 0:
#                 e += 1
#             if e >= len(nums):
#                 return nums

#             if nums[i] % 2 == 1 and i < e:
#                 nums[i], nums[e] = nums[e], nums[i]
#                 e += 1
#             if i <= e:
#                 e = i + 1
#         return nums