class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x, y = 0, n
        res = [-1] * (2 * n)

        for i in range(len(nums)):
            if i % 2 == 0:
                res[i] = nums[x]
                x += 1
            else:
                res[i] = nums[y]
                y += 1
        return res
