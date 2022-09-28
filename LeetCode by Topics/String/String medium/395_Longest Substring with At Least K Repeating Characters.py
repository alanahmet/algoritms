class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        minFreq = min(set(s), key=s.count)
        if s.count(minFreq) >= k:
            return len(s)
        return max(self.longestSubstring(t, k) for t in s.split(minFreq))
