#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> transformArray(vector<int> &nums) {
        for (int i = 0; i < nums.size(); i++) {
            nums[i] &= 1;
        }
        sort(nums.begin(), nums.end());
        return nums;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    Solution sol;
    vector<int> input = {1, 2, 3, 4};
    vector<int> ans = sol.transformArray(input);

    for (int i: ans) {
        cout << i << "\n";
    }

    return 0;
}