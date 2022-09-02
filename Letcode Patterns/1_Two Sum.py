class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i, j in enumerate(nums):
            g = target - j
            if dic.get(g) is not None:
                return [dic[target - j], i]
            dic[j] = i