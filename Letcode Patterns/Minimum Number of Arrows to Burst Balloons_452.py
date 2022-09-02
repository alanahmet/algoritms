class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrow, res = float('-inf'), 0

        for x0, x1 in sorted(points, key=lambda x: x[1]):
            if x0 > arrow:
                res += 1
                arrow = x1

        return res
