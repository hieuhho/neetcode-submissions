class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            s_ord = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                s_ord[idx] += 1
            anagrams[str(s_ord)].append(s)
        res = []
        for k, v in anagrams.items():
            res.append(v)
        return res