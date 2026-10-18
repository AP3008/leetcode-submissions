class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = {}
        for word in strs:
            nW = "".join(sorted(word))
            if nW not in res:
                res[nW] = []
            res[nW].append(word)
        return list(res.values())