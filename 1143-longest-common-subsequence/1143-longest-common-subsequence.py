class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
       # We have a 2D dp, with text1 as the rows, and text2 and the cols
       # Each index in the dp represents the longest common subsequence of that string with the indexes corresponding to the indexes in the string. 
       # We want to pad this dp to handle basecases, at the beginning the array will be 0's

       # dp[i][j]  is the LCS length of the first i characters of text1 and the first j characters of text2

        ROW, COL = len(text1), len(text2)
        dp = [[0] * (COL+1) for _ in range((ROW+1))]

        for i in range(1,ROW+1):
            for j in range(1, COL+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                # Checking if it makes sense to not include text1[i]
                dp[i][j] = max(dp[i][j], dp[i-1][j])
                # Checking if it makes more sense to not include text2[j]
                dp[i][j] = max(dp[i][j], dp[i][j-1])
        return dp[ROW][COL]

