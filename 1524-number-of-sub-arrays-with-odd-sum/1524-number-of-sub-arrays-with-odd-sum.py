class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
       # We can do backtracking only choosing to keep odd numbers, or pass on the current odd number. But since arr.length is between 10^5 that is too inefficient of a solution.

       # We can try to have a dp array, keeping track of the number of odd sums seen. If the current number arr[i] is odd we can increase the value at that dp[i] by 1, we can also use a prefix sum that is just collecting the sum of the array and as we go through... If we add on odd to an even we always get an odd number (2k+(2k+1)), if we add an even to even it's even, odd + odd = even using this logic we can just keep track of the number of odd and even numbers we have seen.

       # HAD TO CHECK SOLUTIONS:
       # DP on parity 
       # If x is even we keep track of all even numbers seen and increment the even parities by one. If we find an odd number we need to flip the relation because all of the previous odd partities become even, and even odd. So what we need to understand is that if x is even parity is unchanged. 
        MOD = 10**9+7
        odd = even = ans = 0
        for x in arr:
            if x % 2 == 1:
                odd,even = even+1, odd
            else:
                even+=1 
            ans = (ans+odd)%MOD
        return ans 
        

