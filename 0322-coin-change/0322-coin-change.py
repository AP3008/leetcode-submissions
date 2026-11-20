class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # DP problem not greedy. 
        # We want each value except the first one dp[amount] to store inf and we then see how many ways there are to reach the spot iterating backwards, so our answer will be held in dp[0] at the end for the min amount of ways to reach. 
        dp = [amount+1] * (amount+1)
        res = amount+1 
        dp[amount] = 0
        for i in range(amount, -1,-1):
            for c in coins:
                if (i-c) >= 0:
                    dp[i-c] = min(dp[i-c], dp[i] + 1)
        return dp[0] if dp[0] != amount+1 else -1
