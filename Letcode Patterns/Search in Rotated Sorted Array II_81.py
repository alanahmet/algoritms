class Solution:
    def search(self, nums: [int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        if len(nums) == 1 and nums[0] == target: return True
        ind = nums[l] > target

        def bc(l, r):
            m = (r + l) // 2
            print(l, m, r)
            if l < r:
                if nums[l] == target:
                    return True
                if not nums[m] > target or ind:
                    ind = nums[m + 1] > target
                    return bc(m + 1, r)
                else:
                    return bc(l, m)
                return False

        return bc(l, r)


print(Solution().search([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1],2))