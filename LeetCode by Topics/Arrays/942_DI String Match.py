class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res, minn, maxx = [], 0, len(s)

        for c in s:
            if c == 'I':
                res.append(minn)
                minn += 1
            else:
                res.append(maxx)
                maxx -= 1

        return res + [minn]