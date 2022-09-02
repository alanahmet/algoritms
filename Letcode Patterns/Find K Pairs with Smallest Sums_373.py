class Solution:
    def kSmallestPairs(self, nums1: [int], nums2: [int], k: int) -> [[int]]:
        res = []

        def bc(fi, si):
            if len(res) == k or len(nums1) <= fi or len(nums2) <= si:
                return 0

            res.append([nums1[fi], nums2[si]])
            if len(nums1) > fi + 1 and len(nums2) > si + 1:
                if nums1[fi + 1] < nums2[si + 1]:
                    return bc(fi + 1, 0) + bc(fi, si + 1)
                else:
                    return bc(fi, si + 1) + bc(fi + 1, 0)
            elif len(nums1) <= fi + 1:
                return bc(0, si + 1)
            elif len(nums2) <= si + 1:
                return bc(fi + 1, 0)

        bc(0, 0)
        return res