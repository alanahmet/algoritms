class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = bisect_left(nums, target)
        if l == len(nums) or nums[l] != target:
            return -1, -1
        r = bisect_right(nums, target) - 1
        return l, r

#         l, r = 0, len(nums) - 1

#         while l <= r:
#             mid = (l + r) // 2
#             if nums[mid] > target:
#                 r = mid - 1
#             if nums[mid] < target:
#                 l = mid + 1
#             if nums[mid] == target:
#                 if mid - 1 >= 0 and nums[mid - 1] == target:
#                     return [mid - 1, mid]
#                 if mid + 1 < len(nums) and nums[mid + 1] == target:
#                     return [mid, mid + 1]
#                 return [mid, mid]

#         return [-1, -1]
