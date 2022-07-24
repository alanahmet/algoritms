class Solution(object):
    def findDuplicate(self, nums):
        singular = set()
        for i in nums:
            if i in singular:
                return i
            else:
                singular.add(i)