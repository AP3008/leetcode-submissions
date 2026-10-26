class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # trivial solution: square elements in array and sort
        return sorted([x**2 for x in nums])