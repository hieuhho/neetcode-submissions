class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        ans_len = 0
        # check from middle
        for i in range(len(s)):
            # check odd palindrome
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > ans_len:
                    ans = s[l:r + 1]
                    ans_len = r - l + 1
                l -= 1
                r += 1
            
            # check even palindrome
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > ans_len:
                    ans = s[l:r + 1]
                    ans_len = r - l + 1
                l -= 1
                r += 1
        return ans