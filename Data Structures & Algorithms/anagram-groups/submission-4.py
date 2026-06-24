class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            char_count = [0] * 26
            for i in word:
                char_count[ord(i) - ord("a")] += 1
            res[str(char_count)].append(word)
        return list(res.values())