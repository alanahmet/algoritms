class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count, j = Counter(s1), 0
        for i, v in enumerate(s2):
            count[v] -= 1
            while count[v] < 0:
                count[s2[j]] += 1
                j += 1
            if i - j + 1 == len(s1):
                return True

        return False
