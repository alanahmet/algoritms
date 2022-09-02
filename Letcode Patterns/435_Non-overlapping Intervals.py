class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        curEnd, ans = float('-inf'), 0
        for i in sorted(intervals, key=lambda x: x[1]):
            if curEnd <= i[0]:
                curEnd = i[1]
            else:
                ans += 1
        return ans
