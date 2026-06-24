class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_alphabet = [0] * 26
        s2_alphabet  = [0] * 26
        s1_dict = {}
        for letter in s1:
            s1_alphabet[ord(letter) - ord("a")] += 1
            s1_dict[letter] = 1 + s1_dict.get(letter, 0)
        l = 0

        for r in range(len(s2)):

            if not s1_dict.get(s2[r]):
                l = r + 1
                s2_alphabet  = [0] * 26
                continue
            s2_alphabet[ord(s2[r]) - ord("a")] += 1
            if len(s1) < (r - l + 1):
                s2_alphabet[ord(s2[l]) - ord("a")] -= 1
                l += 1

            if len(s1) == (r - l + 1):
                if s2_alphabet == s1_alphabet:
                    return True

        return False