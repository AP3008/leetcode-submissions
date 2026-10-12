class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1 
        profit = 0 
        while r < len(prices):
            curr = prices[r] - prices[l]
            if curr > profit:
                profit = curr
            if prices[l] > prices[r]:
                l = r
                r+=1 
            else:
                r+=1
        return profit  
        