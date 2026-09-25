class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or not t:
            return ""
        
        tCount, window = {}, {}

        for c in t:
            tCount[c] = tCount.get(c, 0) + 1
        
        current, need = 0, len(tCount)
        res = [-1, -1]
        resLen = float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in tCount and window[c] == tCount[c]:
                current += 1
            
            while current == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                window[s[l]] -= 1
            
                if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                    current -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""