class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen_s = {}
        seen_t = {}
        for i in s:
            seen_s[i] = seen_s.get(i, 0) + 1
        for i in t:
            seen_t[i] = seen_t.get(i, 0) + 1
        
        if seen_s != seen_t:
            return False
        return True