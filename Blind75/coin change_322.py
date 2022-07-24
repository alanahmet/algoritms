class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(len(dp)):
            for c in coins:
                if amount - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        return dp[amount] if dp[amount] != amount + 1 else -1
    """
        coins = sorted(coins)

        def helper(coin, step):
            print(f"c: {coin} s:{step}")
            if coin == 0:
                return step
            if coin < 0:
                return -1
            step += 1
            for i in range(len(coins) - 1, -1, -1):
                print(f"Coins {coins[i]}")
                res = helper(coin - coins[i],step)
                if res >= 1:
                    return res
            return -1
        return helper(amount,0)"""


Sol = Solution()
sol = Sol.coinChange([186, 419, 83, 408], 6249)
print(sol)
