class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        if len(s) != len(t):
            return False
        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1

        for i in t:
            if i in t_dict:
                t_dict[i] += 1
            else:
                t_dict[i] = 1
                
        for letter, occurance in s_dict.items():
            if letter not in t_dict or t_dict[letter] != occurance:
                return False
        return True