class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
       # Graph problem: we want to have an adj. list of each pattern a word falls into. So we perform a dfs on the pattern until we get a pattern. We store the best parttern in res and compare the min of a successful dfs to see if we got a valid path. 
       # AMENDMENT: DO NOT USE DFS for this, this is a shortest path of an unqweighted graph so we should be using BFS with a queue instead 
        if endWord not in wordList: return 0
        adj = {}
        wordList.append(beginWord)
        for w in wordList:
            for i in range(len(w)):
                store = w[:i] + "*" + w[i+1:]
                if store not in adj:
                    adj[store] = []
                adj[store].append(w)
        seen = set()
        res = 1 
        q = deque()
        q.append(beginWord)
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord: return res 
                for i in range(len(word)):
                    store = word[:i]+"*"+word[i+1:]
                    for w in adj[store]:
                        if w not in seen:
                            seen.add(w)
                            q.append(w)
            res+=1 
        return 0

