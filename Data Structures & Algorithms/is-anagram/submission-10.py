class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_freq = defaultdict(int)
        t_freq = defaultdict(int)
        for i in s:
            s_freq[i] += 1
        
        for i in t:
            t_freq[i] += 1

        return s_freq == t_freq

