class Solution:
    def frequencySort(self, s: str) -> str:
        freq, res = collections.Counter(s).most_common(), ''

        for v, f in freq:
            res = res + v * f
        return res
