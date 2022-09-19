class Solution:
    def numJewelsInStones(self, j: str, s: str) -> int:
        return sum(map(j.count, s))

        jew_dic = {i for i in jewels}
        res = 0
        for i in stones:
            if i in jew_dic:
                res += 1
        return res