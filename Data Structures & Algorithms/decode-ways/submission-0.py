class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        # dp0 = count up to i - 2, dp1 = count up to i - 1
        dp0 = 1
        dp1 = 0 if s[0] == "0" else 1
        for i in range(1, len(s)):
            count = 0
            # check single digit, if valid then ALL previous count is valid
            if s[i] != "0":
                count += dp1

            # check double digit, if double digit is valid then ALL previous count up to i - 2 is valid
            double_digit = int(s[i-1:i+1]) # i+1 because it is exclusive ie s= "123", i = 1 ==> s[i-1:i] = "1" but s[i-1:i+1] = "12"
            if s[i-1] != "0" and 10 <= double_digit <= 26:
                count += dp0

            dp0 = dp1
            dp1 = count
        return dp1