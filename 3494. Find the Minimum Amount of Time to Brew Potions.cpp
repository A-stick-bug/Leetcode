// https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions
// Dynamic programming, loop twice per row
// Note: a 5000x5000 array overflows the stack

#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    long long minTime(vector<int> &skill, vector<int> &mana) {
        int n = skill.size();
        int m = mana.size();

        // 1-indexed
        vector<vector<long long>> dp(m + 1, vector<long long>(n + 1, 0));

        for (int i = 1; i <= m; i++) {
            // loop forwards to get the min last value in this row
            for (int j = 1; j <= n; j++) {
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) + 1LL * skill[j - 1] * mana[i - 1];
            }
            // use the min last value to construct the rest of the row
            for (int j = n - 1; j >= 0; j--) {
                dp[i][j] = dp[i][j + 1] - 1LL * mana[i - 1] * skill[j];
            }
        }
        return dp[m][n];
    }
};


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);


    return 0;
}