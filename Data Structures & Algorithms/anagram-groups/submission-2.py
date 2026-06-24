class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        occur = {}
        for word in strs:
            freq = [0] * 26
            for letter in word:
                inx = ord(letter) - ord("a")
                freq[inx] += 1
            freq_str = str(freq)
            if freq_str in occur:
                occur[freq_str].append(word)
            else:
                occur[freq_str] = [word]
        return list(occur.values())