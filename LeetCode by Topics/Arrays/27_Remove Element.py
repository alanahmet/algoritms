class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0

        for num in nums:
            if num != val:
                nums[i] = num
                i += 1

        return i

        # nVal = 0  # non val index
        # for i in range(len(nums)):
        #     while nVal < len(nums) and nums[nVal] == val:
        #         nVal += 1
        #     if nVal >= len(nums):
        #         break
        #     if nums[i] == val:
        #         nums[i], nums[nVal] = nums[nVal], nums[i]
        #         nVal += 1
        #
        #     if i >= nVal:
        #         nVal += 1
        #
        # for i in range(len(nums)):
        #     if nums[i] == val:
        #         return i
