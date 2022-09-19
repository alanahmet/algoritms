class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans, deq = [], deque()

        for i, v in enumerate(nums):
            while deq and v > deq[-1]:
                deq.pop()

            deq.append(v)

            if i >= k and nums[i - k] == deq[0]:
                deq.popleft()

            if i >= k - 1:
                ans.append(deq[0])
        return ans
