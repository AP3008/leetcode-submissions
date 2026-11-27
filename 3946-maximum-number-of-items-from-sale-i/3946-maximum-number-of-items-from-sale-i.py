class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        # Not my own solution 
        # The goal is to get as many copies as possible, bought + free together for at most budget. 
        
        factors, prices = zip(*items)
        have = [0] * (max(factors)+1) # have[f]: items with factor f 
        for factor in factors:
            have[factor]+=1 
        gains = {factor : sum(have[factor::factor]) for factor in set(factors)} # Every factor-th call is a multiple
        cheapest = min(prices)
        best = [money // cheapest for money in range(budget+1)] # no first copies: everything goes to the cheapest item 
        for factor, price in items: 
            if (gain := gains[factor]) > price // cheapest:
                for money in range(budget, price-1,-1):
                    best[money] = max(best[money], best[money-price]+gain)
        return best[budget]