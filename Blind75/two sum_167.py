class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while r > l:
            s = numbers[r] + numbers[l]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            else:
                r -= 1
