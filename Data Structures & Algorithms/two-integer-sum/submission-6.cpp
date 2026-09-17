class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> remains;
        for (int i{0}; i < nums.size(); i++) {
            if (remains.find(nums[i]) != remains.end()) {
                return {remains[nums[i]], i};
            }
            int diff = target - nums[i];
            remains[diff] = i;
        }
        return {};
    }
};
