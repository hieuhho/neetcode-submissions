class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> mapping;
        for (auto i: nums)
            mapping[i]++;
        
        for (auto i: mapping) {
            if (i.second > 1) {
                return true;
            }
        }
        return false;
    }
};