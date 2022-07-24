class Solution(object):
    def singleNumber(self, nums):
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1

        for key, val in dic.items():
            if val == 1: return key