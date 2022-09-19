class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        res = False

        for i in range(len(goal)):
            if goal[i] == s[0]:
                res = True if goal[i:] == s[:len(s) - i] and s[len(s) - i:] == goal[:i] else res
        return res