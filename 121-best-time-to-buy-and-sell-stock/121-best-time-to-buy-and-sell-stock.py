class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        i, smallest = 0, prices[0]
        profit = 0
        while i < size:
            smallest = min(smallest, prices[i])
            _profit = prices[i]-smallest
            profit = max(profit, _profit)
            i += 1
        return profit