class Solution:
    def shortestToChar(self, S, C):
        c_pos = []
        res = [-1] * len(S)

        for i in range(len(S)):
            if S[i] == C:
                c_pos.append(i)

        if len(c_pos) < 2:
            return [abs(i - c_pos[0]) for i in range(len(S))]

        r, l = c_pos[:2]
        index = 2

        for i in range(len(S)):
            res[i] = min(abs(r - i), abs(l - i))

            if i == l and index < len(c_pos):
                r, l = l, c_pos[index]
                index += 1

        return res