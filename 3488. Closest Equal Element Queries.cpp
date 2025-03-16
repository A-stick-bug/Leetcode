// https://leetcode.com/problems/closest-equal-element-queries/
// Map + binary search

#include <bits/stdc++.h>

using namespace std;

#define all(x) x.begin(),x.end()

class Solution {
public:
    vector<int> solveQueries(vector<int> &nums, vector<int> &queries) {
        unordered_map<int, vector<int>> loc;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            loc[nums[i]].push_back(i);
        }

        vector<int> res;
        for (int idx: queries) {
            int val = nums[idx];
            if (loc[val].size() == 1) {  // unique
                res.push_back(-1);
                continue;
            }
            int i = distance(loc[val].begin(), lower_bound(all(loc[val]), idx));
            int ans = 1 << 30;
            if (i != 0) {
                ans = min(ans, idx - loc[val][i - 1]);
            } else {
                ans = min(ans, idx + n - loc[val][loc[val].size() - 1]);
            }
            if (i != loc[val].size() - 1) {
                ans = min(ans, loc[val][i + 1] - idx);
            } else {
                ans = min(ans, loc[val][0] + n - idx);
            }
            res.push_back(ans);
        }
        return res;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);


    return 0;
}