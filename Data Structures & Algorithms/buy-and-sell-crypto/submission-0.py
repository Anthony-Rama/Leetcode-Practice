class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0

        # move left pointer when prices[r] < prices[l]
        
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            profit = max(profit, prices[r] - prices[l])

        return profit 