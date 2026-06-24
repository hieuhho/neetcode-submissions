class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for word in strs:
            abc = [0] * 26
            for i in word:
                abc[ord(i) - ord("a")] += 1
            seen[tuple(abc)].append(word)
        return list(seen.values())