class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        # Perform a bfs on every letter in word to see if there is some combination to see if the word exists. We split the word and put it into a set, then we start building a set....
        # Forget the first idea it is much simpler than that. We want to find the first letter of the string in the array then perform a DFS on that, if it is connected to the following char, then we DFS on that char, and this continue until the index we pass through the bfs function suprasses the size of the string, at which point means we found the word and can return true 

        ROW = len(board)
        COL = len(board[0])
        visit = set()
        def dfs(r,c,i):
            if i >= len(word): return True 
            if (ROW <= r or
                COL <= c or
                0 > r or
                0 > c or
                (r,c) in visit or
                word[i] != board[r][c]):
                return False
            visit.add((r,c))
            res = (dfs(r+1,c,i+1) or 
                    dfs(r-1,c,i+1) or
                    dfs(r,c+1,i+1) or
                    dfs(r,c-1,i+1))
            visit.remove((r,c))
            return res
        for r in range(ROW):
            for c in range(COL):
                if dfs(r,c,0):
                    return True
        return False 

