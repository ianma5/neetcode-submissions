class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        minBuy = prices[0]
        maxProfit = 0

        for price in prices:
            if price < minBuy:
                minBuy = price
            elif price - minBuy > maxProfit:
                maxProfit = price - minBuy
        return maxProfit