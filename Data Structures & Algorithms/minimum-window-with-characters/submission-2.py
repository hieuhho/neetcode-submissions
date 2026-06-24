class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        t_count, window_count = {}, {}
        res_window, res_len = [-1, -1], float("infinity")

        for letter in t:
            t_count[letter] = 1 + t_count.get(letter, 0)

        have, need = 0, len(t_count)
        l = 0
        for r in range(len(s)):
            letter = s[r]
            window_count[letter] = 1 + window_count.get(letter, 0)

            if letter in t_count and window_count[letter] == t_count[letter]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res_window = [l, r]
                    res_len = r - l + 1

                window_count[s[l]] -= 1
                if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        l, r = res_window
        return s[l: r + 1] if res_len != float("infinity") else ""