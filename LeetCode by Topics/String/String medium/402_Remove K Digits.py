class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ans = []

        for n in num:
            while k and ans and ans[-1] > n:
                ans.pop()
                k -= 1
            if n != '0' or ans:
                ans.append(n)

        if k > 0:
            ans = ans[0:-k]

        return "".join(ans) if ans else '0'
