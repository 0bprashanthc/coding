class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length == 0:
            return []
        left, right = 0, 1
        max_profit = 0
        while right < length:
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                if profit > max_profit:
                    max_profit = profit
            else:
                left = right
            right = right + 1
        return max_profit