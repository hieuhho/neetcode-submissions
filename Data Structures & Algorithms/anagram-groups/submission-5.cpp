class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        /*
        for each str, convert to alpha
        add str to alpha code

        for each alphacode, add val (str) to array
        return array
        */
        unordered_map<string, vector<string>> alphanumeric;
        for (const auto& s: strs) {
            vector<int> count(26, 0);
            for (auto c: s) {
                count[c - 'a']++;
            }
            string key = to_string(count[0]);
            for (int i{1}; i < 26; i++) {
                key += ',' + to_string(count[i]);
            }
            alphanumeric[key].push_back(s);
        }

        vector<vector<string>> result;
        for (const auto& group: alphanumeric) {
            result.push_back(group.second);
        }
        return result;
    }
};
