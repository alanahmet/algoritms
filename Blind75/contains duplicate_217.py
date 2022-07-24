class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False

"""
        unique_list = set()
        list_lenght =len(unique_list) 
        for i in nums:
            unique_list.add(i)
            if len(unique_list) == list_lenght:
                return True
            list_lenght = len(unique_list) 
        return False
        """