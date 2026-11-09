class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # backtracking, decision tree; choose to take a value or not to take a value. 
        # We want to increment through candidates when we don't choose to use a value but stay on the same index if we are using the value. We have a current list, which we pop() the last element we added and then run a dfs again. 

        res = []
        curr = []

        def backtrack(i, summ):
            if i >= len(candidates) or summ >= target:
                if summ == target:
                    res.append(curr.copy())
                return 
            curr.append(candidates[i])
            # we are keeping this value 
            backtrack(i,summ+candidates[i])
            curr.pop()
            backtrack(i+1,summ)

        backtrack(0,0)
        return res 