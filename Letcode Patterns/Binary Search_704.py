class Solution:
    def search(self, nums: [int], target: int) -> int:
        self.res = -1

        def bs(arr, index):
            if len(arr) == 1 and arr[0] == target:
                self.res = index

            cp = len(arr) // 2
            if len(arr) > 1:
                bs(arr[:cp], index)
                bs(arr[cp:], index + cp)
        bs(nums, 0)
        return self.res
