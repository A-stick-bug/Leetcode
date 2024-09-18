/*
 * https://leetcode.com/problems/find-the-maximum-sequence-value-of-array
 * Tricky knapsack DP with bitmask
 * For each possible value/mask, find both the min and max number of values needed to reach it
 * If min <= K <= max, it is a valid mask for that half of the subsequence
 * Note: since we are using bitwise OR, push DP must be used
 *
 * TC: O(N^2 * 128)
 * SC: O(N)
 */

int maxValue(vector<int>& nums, int k) {
    const int MX = 1 << 7; // 2^7 = 128
    int best = 0;
    int inf = INT_MAX - 1000;
    int n = nums.size();

    for (int mid = 1; mid < n; ++mid) {  // try all split points and select K from both sides
        vector<int> a1(nums.begin(), nums.begin() + mid);
        vector<int> a2(nums.begin() + mid, nums.end());

        if (a1.size() < k || a2.size() < k)  // too short
            continue;

        // minimum number of values to achieve mask of `i`
        vector<int> dp1(MX, inf);
        dp1[0] = 0;  // base case: 0 moves to have nothing
        for (int val : a1) {
            for (int i = MX - 1; i >= 0; --i) {
                dp1[i | val] = min(dp1[i | val], dp1[i] + 1);
            }
        }

        // maximum number of values to achieve mask of `i`
        vector<int> dp11(MX, -inf);
        dp11[0] = 0;
        for (int val : a1) {
            for (int i = MX - 1; i >= 0; --i) {
                dp11[i | val] = max(dp11[i | val], dp11[i] + 1);
            }
        }

        // repeat for `a2`
        vector<int> dp2(MX, inf);
        dp2[0] = 0;  // base case: 0 moves to have nothing
        for (int val : a2) {
            for (int i = MX - 1; i >= 0; --i) {
                dp2[i | val] = min(dp2[i | val], dp2[i] + 1);
            }
        }

        // `a2` max
        vector<int> dp22(MX, -inf);
        dp22[0] = 0;
        for (int val : a2) {
            for (int i = MX - 1; i >= 0; --i) {
                dp22[i | val] = max(dp22[i | val], dp22[i] + 1);
            }
        }

        // get best pair of masks
        for (int mask1 = 1; mask1 < MX; ++mask1) {
            for (int mask2 = 1; mask2 < MX; ++mask2) {
                if (dp1[mask1] <= k && k <= dp11[mask1] && dp2[mask2] <= k && k <= dp22[mask2]) {
                    best = max(best, mask1 ^ mask2);
                }
            }
        }
    }
    return best;
}
