class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        # dp0 = count up to i - 2, dp1 = count up to i - 1
        dp0 = 1
        dp1 = 1
        for i in range(1, len(s)):
            count = 0
            # check single digit, if valid then ALL previous count is valid
            if s[i] != "0":
                count += dp1

            # check double digit, if double digit is valid then ALL previous count up to i - 2 is valid
            if s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'):
                count += dp0

            # dp0 then slide over (prev_max)
            dp0 = dp1
            # dp1 then become the current max
            dp1 = count
        return dp1