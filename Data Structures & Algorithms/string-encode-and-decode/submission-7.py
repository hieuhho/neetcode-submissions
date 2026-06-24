class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res
    
    def decode(self, s: str) -> List[str]:
        ans = []
        # set starting index
        i = 0
        while i < len(s):
            # set second index
            j = i
            # move the second index to till word start
            while s[j] != "#":
                j += 1
            # the word length is between starting & finishing
            word_length = int(s[i:j])
            # move first index to where word start
            i = j + 1
            # second index is the start + word_length
            j = i + word_length
            ans.append(s[i:j])
            # move the first index to the next word
            i = j
        return ans
            