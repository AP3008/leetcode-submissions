class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        # IDEA: 
        # Count how many items have each factor using a freq. array 
        # For every factor f, count all items whose factors are multiples of f. Subtract 1 to get the maximum number of free copies for each item. 
        # Find the minimum item price (minP). Store each item with a positive gain as (price, gain) and sort them by price. 
        # Process the sorted items 
            # A purchase that gives a free copy adds 2 items 
            # Buy these copies only when price <= 2 * minP
            # Buy as many as the remaining budget allows, without exceeding the item's gain. 
        # Spend the remaining budget on the cheapest item, where each purchase adds 1 item. 
        # return the total number of items. 

        n = len(items)
        cnt = [0] * (n+1)
        for f, p in items:
            cnt[f] += 1
        
        mult = [0] * (n+1)
        for f in range(1, n+1):
            for m in range(f, n+1, f):
                mult[f] += cnt[m]
        min_p = min(p for f, p in items)
        cand = []

        for f, p in items:
            g = mult[f]-1
            if g > 0:
                cand.append((p,g))
        cand.sort()
        spent = 0 
        total = 0 
        B = budget 
        for p, g in cand:
            if p > 2 * min_p:
                break 
            can = min(g, (B-spent)//p)
            total += can * 2
            spent += can*p
        total += (B-spent)//min_p
        return total 