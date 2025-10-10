class Solution {
public:
    vector<int> maxKDistinct(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        nums.erase(unique(nums.begin(), nums.end()), nums.end());
        sort(nums.begin(), nums.end(), greater<>());
        vector<int> res;
        for (int i = 0; i < min(k, (int)nums.size()); i++)
            res.push_back(nums[i]);
        return res;
    }
};