class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length())
            return false;

        unordered_map <char, int> seen_s;
        unordered_map <char, int> seen_t;
        for (auto i: s)
            seen_s[i]++;
        for (auto j: t)
            seen_t[j]++;

        for (auto i: seen_s) {
            if (i.second != seen_t[i.first]) {
                return false;
            }
        }


        return true;
    }
};
