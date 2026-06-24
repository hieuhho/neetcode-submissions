class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if set(s) != set(t):
            return False
        list_s = list(s)
        list_t = list(t)
        list_s.sort()
        list_t.sort()
        print(list_s)
        print(list_t)
        for idx, x in enumerate(list_s):
            if list_s[idx] != list_t[idx]:
                return False
        return True