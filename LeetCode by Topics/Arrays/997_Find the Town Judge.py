class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        tr = dict(trust)
        jud = -1

        for i in tr.keys():
            j = tr[i]

            c = 0  # check inf loop
            while j in tr:
                j = tr[j]
                c += 1
                if c == n:
                    return -1

            if jud == - 1:
                jud = j
            elif jud != j:
                return - 1

        return jud
