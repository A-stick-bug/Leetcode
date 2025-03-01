// https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/
// standard array DP
// - for each index, we can take one of three elements
// - the one not taken will be split off from the array, there will be at most
//   one element that is split off since we take 2 of three each time

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<unordered_map<int, int>> memo;

    int solve(vector<int> &arr, int idx, int extra) {
        if (idx == arr.size() - 1)
            return max(arr[idx], extra);
        if (idx == arr.size())
            return extra;
        if (memo[idx].count(extra))
            return memo[idx][extra];

        int best = 1 << 30;
        best = min(best, solve(arr, idx + 2, arr[idx + 1]) + max(extra, arr[idx]));
        best = min(best, solve(arr, idx + 2, extra) + max(arr[idx], arr[idx + 1]));
        best = min(best, solve(arr, idx + 2, arr[idx]) + max(arr[idx + 1], extra));

        return memo[idx][extra] = best;
    }

    int minCost(vector<int> &nums) {
        memo.resize(nums.size() + 2);
        if (nums.size() < 3)
            return *max_element(nums.begin(), nums.end());

        return solve(nums, 1, nums[0]);
    }
};


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);


    return 0;
}