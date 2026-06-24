class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        ans = 0
        most_freq = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            most_freq = max(most_freq, count[s[r]])
            while (r - l + 1) - most_freq > k:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, (r - l + 1))
        return ans