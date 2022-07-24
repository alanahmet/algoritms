class Solution(object):
    def containsDuplicate(self, nums):
        num_hash = set()
        for i in nums:
            if i in num_hash:
                return True
            num_hash.add(i)
        return False

#  return len(nums) != len(set(nums))
