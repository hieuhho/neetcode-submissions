class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> seen;
        for (int n: nums)
            seen[n] = seen[n] + 1;
        
        vector<vector<int>> freq(nums.size() + 1);
        for (const auto& n: seen)
            freq[n.second].push_back(n.first);

        vector<int> result;
        for (int i = freq.size() - 1; i > 0; --i) {
            for (int n: freq[i]) {
                result.push_back(n);
                if (result.size() == k) {
                    return result;
                }
            }
        }
        return result;
    }
};
