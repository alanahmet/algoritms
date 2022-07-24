class Solution:
    def search(self, nums: [int], target: int) -> int:
        l, r = 0, len(nums) - 1
        res = -1
        while l <= r:
            print(f"r: {r} , l: {l}")
            mid = (l + r) // 2
            if l - r <= 3:
                print(nums[l:r])
                if target in nums[l:r+1 ]:
                    return nums[l:r+1].index(target)
                else:
                     return res
            if nums[mid] == target:
                return mid
            if nums[mid] >= target >= nums[l]:
                r = mid + 1
                print("a")
            else:
                print(mid)
                l = mid - 1
                print(l)
        return res


Ex = Solution()
ex = Ex.search([1], 1)
print(ex)