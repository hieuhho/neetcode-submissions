class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = defaultdict(int)
        for i in range(len(s)):
            freq[s[i]] += 1
            freq[t[i]] -= 1

        for val in freq.values():
            if val != 0:
                return False
        return True

