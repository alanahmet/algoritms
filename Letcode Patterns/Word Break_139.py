class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        if not wordDict or not s:
            return False
        words = set(wordDict)

        @lru_cache(None)
        def bc(rs):
            if rs in words:
                return True
            return any(rs[:i] in words and bc(rs[i:]) for i in range(len(s)))

        return bc(s)
