class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        dp = [0] + [amount + 1] * amount
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i], dp[i - c] + 1)
        return -1 if dp[amount] == amount + 1 else dp[amount]


"""     my dummy
        coins.sort()
        coins = coins[::-1]
        self.isfind, self.res = False, float("inf")

        def bc(noc, rema):
            print(rema)
            if rema == 0:
                self.res = min(noc, self.res)
                self.isfind = True
            if rema > 0:
                for i in coins:
                    if rema - i >= 0:
                        bc(noc + 1, rema - i)
                    if i == coins[0] and self.isfind:
                        break

        bc(0, amount)
        return self.res
"""
