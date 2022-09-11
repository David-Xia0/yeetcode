from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        profit = 0
        for price in prices:
            currentProfit = price - low
            if currentProfit > profit:
                profit = currentProfit

            if price < low:
                low = price

        return profit

