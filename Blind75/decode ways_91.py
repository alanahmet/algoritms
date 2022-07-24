class Solution:
    def numDecodings(self, s: str) -> int:
        sol = 1 if int(s[0]) > 0 else 0
        for i in range(1, len(s)):
            if int(s[i]) != 0:
                if int(s[i - 1]) != 0:
                    total = str(s[i - 1]) + str(s[i])
                    if int(total) < 27:
                        sol += 1
        return sol
sol = Solution()
Sol = sol.numDecodings("27")
print(Sol)