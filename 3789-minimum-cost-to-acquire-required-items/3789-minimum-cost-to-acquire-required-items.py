class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # The question is a decision tree choosing when to use cost both, cost1 individually, etc. We can try and do this via backtracking where we choose one of the three choices, and the minimum of all outputs that satisfy both need1 and need2 are the correct answers. (O(3^n))

        # Instead of using backtracking and finding all solutions, I think we can design an iterative solution that works better. Start by having a have1 and have2, once have1 and have2 are equal to the need, we can return the minimum we have calculated. We want to check if costBoth is less than cost1 and cost2, if it is, since we need at least need for both the max of needs * costBoth will give use the answer in constant time. 

        # This solution is just based of reasoning 

        # if need1 and need2 are zero we return 0
        if not need1 and not need2: return 0 
        # We compute the lesser of the two needs so we can use it in our final expression
        lower = min(need1, need2)
        # 1. If the costBoth is less than buying both cost1 and cost2, we can buy all of lower from there, meaning now need1 or need2 is completley clear 
        # 2. we add on the difference of need1-lower * (the less of costBoth vs. cost1), if lower is already need1, then we get 0 * cost which is 0 since we already have all of need1
        # 3. We do the same thing but with need2 and cost2, so we can buy the remaining items we didn't have. 
        return lower*min(costBoth,cost1+cost2) + (need1-lower)*min(costBoth,cost1)+(need2-lower)*min(costBoth,cost2)