class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []
        for num in nums:
            if not tail or num > tail[-1]:
                tail.append(num)
            else:
                tail[bisect_left(tail, num)] = num
        return len(tail)
