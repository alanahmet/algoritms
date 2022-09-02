class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans, f, s = [], 0, 0

        while f < len(firstList) and s < len(secondList):
            l, r = max(firstList[f][0], secondList[s][0]), min(firstList[f][1], secondList[s][1])
            if l <= r:
                ans.append([l, r])
            if firstList[f][1] < secondList[s][1]:
                f += 1
            else:
                s += 1

        return ans
