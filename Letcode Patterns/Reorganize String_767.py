class Solution:
    def reorganizeString(self, s: str) -> str:
        l = len(s)
        c = Counter(s)
        maxC = max(c.values())

        if maxC > (l + 1) // 2:
            return ''

        if maxC == (l + 1) // 2:
            maxItem = max(c, key=c.get)
            res = [maxItem if i % 2 == 0 else '' for i in range(l)]
            del c[maxItem]
            i = 1
        else:
            res = [''] * l
            i = 0

        for v, count in c.items():
            for _ in range(count):
                res[i] = v
                i += 2
                if i >= l:
                    i = 1
        return ''.join(res)
