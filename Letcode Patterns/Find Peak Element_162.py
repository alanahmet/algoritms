class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def search(l, r):
            if l == r:
                return l
            m = (l + r) // 2
            if nums[m] > nums[m + 1]:
                return search(l, m)
            return search(m + 1, r)
        return search(0, len(nums) - 1)