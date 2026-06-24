class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_table = {}
        t_table = {}
        for i in s:
            s_table[i] = s_table.get(i, 0) + 1
        for i in t:
            t_table[i] = t_table.get(i, 0) + 1
        return s_table == t_table

