class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> mapping;
        for (auto i: nums) {
            if (mapping[i] > 0) {
                return true;
            }
            mapping[i]++;
        }

        return false;
    }
};