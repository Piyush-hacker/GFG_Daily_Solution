class Solution:
   def maxProfit(self, prices):
        min_price, max_profit = prices[0], 0
        for p in prices:
            if p < min_price:
                min_price = p
            elif (mp := p - min_price) > max_profit:
                max_profit = mp
        return max_profit