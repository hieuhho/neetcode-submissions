class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = {}, {}
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] = s1Count.get(ord(s1[i]) - ord('a'), 0) + 1
            s2Count[ord(s2[i]) - ord('a')] = s2Count.get(ord(s2[i]) - ord('a'), 0) + 1
        
        matches = 0
        for i in range(26):
            matches += (1 if s1Count.get(i, 0) == s2Count.get(i, 0) else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            rIndex = ord(s2[r]) - ord('a')
            s2Count[rIndex] = s2Count.get(rIndex, 0) + 1
            if s1Count.get(rIndex, 0) == s2Count.get(rIndex, 0):
                matches += 1
            elif s1Count.get(rIndex, 0) + 1 == s2Count.get(rIndex, 0):
                matches -= 1

            lIndex = ord(s2[l]) - ord('a')
            s2Count[lIndex] = s2Count.get(lIndex, 0) - 1
            if s1Count.get(lIndex, 0) == s2Count.get(lIndex, 0):
                matches += 1
            elif s1Count.get(lIndex, 0) - 1 == s2Count.get(lIndex, 0):
                matches -= 1
            l += 1
        return matches == 26
