class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seenS = {}
        for c in s:
            seenS[c] = seenS.get(c, 0) + 1
        seenT = {}
        for c in t:
            seenT[c] = seenT.get(c, 0) + 1
        return seenS == seenT