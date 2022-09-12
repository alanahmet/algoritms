class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell, hold = 0, float('-inf')

        for p in prices:
            sell = max(sell, hold + p)
            hold = max(hold, sell - p)

        return sell