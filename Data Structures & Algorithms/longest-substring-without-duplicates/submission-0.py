class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        max_len = 0
        l = 0
        for i in range(len(s)):
            while s[i] in my_set:
                my_set.remove(s[l])
                l += 1
            my_set.add(s[i])
            max_len = max(i - l + 1, max_len)
        return max_len
