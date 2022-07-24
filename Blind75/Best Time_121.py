class Solution:
    def maxProfit(self, prices: [int]) -> int:
        lowest = prices[0]
        max_profit = 0
        for stack_value in prices:
            profit = stack_value - lowest
            if profit > max_profit:
                max_profit = profit
            if lowest > stack_value:
                lowest = stack_value
        return max_profit
