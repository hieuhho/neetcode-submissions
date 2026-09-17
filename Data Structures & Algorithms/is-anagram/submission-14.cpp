class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length())
            return false;

        unordered_map <char, int> frequency;
        for (int i{0}; i < s.length(); i++) {
            frequency[s[i]]++;
            frequency[t[i]]--;

        }
        
        for (auto i: frequency) {
            if (i.second != 0) {
                return false;
            }
        }


        return true;
    }
};
