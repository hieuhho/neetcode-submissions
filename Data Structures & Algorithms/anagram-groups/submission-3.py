class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        occur = {}
        for word in strs:
            freq = [0] * 26
            for letter in word:
                inx = ord(letter) - ord("a")
                freq[inx] += 1
            if tuple(freq) in occur:
                occur[tuple(freq)].append(word)
            else:
                occur[tuple(freq)] = [word]
        return list(occur.values())