// https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/description/
// states: [index (implicit)][subarray #][length of subarray (capped at 3)]

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxSum(vector<int> &nums, int k, int m) {
        int n = nums.size();
        int inf = 1 << 30;

        int prev[k + 1][m + 1];
        for (int i = 0; i <= k; i++) {
            for (int j = 0; j <= m; j++) {
                prev[i][j] = -inf;
            }
        }
        prev[0][0] = 0;
        prev[0][1] = nums[0];

        int ans = -inf;
        ans = max(ans, prev[k - 1][m]);

        for (int i = 1; i < n; i++) {
            int dp[k + 1][m + 1];
            for (int x = 0; x <= k; x++) {
                for (int y = 0; y <= m; y++) {
                    dp[x][y] = -inf;
                }
            }

            for (int cur = 0; cur <= k; cur++) {
                if (cur >= k) {
                    continue;
                }

                // skip
                dp[cur][0] = max(prev[cur][0], cur > 0 ? prev[cur - 1][m] : -inf);

                // start new one here
                dp[cur][1] = nums[i] + (cur > 0 ? prev[cur - 1][m] : -inf);

                for (int le = 1; le <= m; le++) {
                    dp[cur][le] = max(dp[cur][le], prev[cur][le - 1] + nums[i]);
                }
                dp[cur][m] = max(dp[cur][m], prev[cur][m] + nums[i]); // m to m special transition
            }

            for (int x = 0; x <= k; x++) {
                for (int y = 0; y <= m; y++) {
                    prev[x][y] = dp[x][y];
                }
            }
            ans = max(ans, prev[k - 1][m]);
        }
        return ans;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);


    return 0;
}