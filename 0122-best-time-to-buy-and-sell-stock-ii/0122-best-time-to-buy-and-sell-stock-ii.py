class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right = 1
        profit = 0

        while right < len (prices):
            if prices[right] - prices[right - 1] > 0 :
                profit += prices[right] - prices[right - 1]

            right += 1

        return profit
        