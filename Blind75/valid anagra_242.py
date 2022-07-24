class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) is not len(t):
            return False
        t_set = {}

        for i in t:
            t_set[i] = 1 + t_set.get(i, 0)

        for i in s:
            if i in t_set:
                t_set[i] -= 1
                if t_set[i] == 0:
                    t_set.pop(i)

        return True if len(t_set) < 1 else False


print(Solution().isAnagram("anagram", "nagaram"))
