class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        ans = 0
        l = 0
        for r in range(len(s)):
            while s[r] in my_set:
                my_set.remove(s[l])
                l += 1
            my_set.add(s[r])
            ans = max(ans, r - l + 1)
        return ans
