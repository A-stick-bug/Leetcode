// https://leetcode.com/problems/maximum-total-from-optimal-activation-order
// - Intuitively, we start by activating the elements with lowest limit
//   - This avoids permanently inactivating the elements less than it
//   - This also makes each unique limit value independent since the ones with
//     less limit will turn themselves off after reaching the limit
// - For ties, we just take the ones with the highest value

class Solution {
public:
    long long maxTotal(vector<int>& value, vector<int>& limit) {
        int n = value.size();
        vector<vector<int>> mp(n+1);

        long long total = 0;
        for (int i = 0; i < n; i++) {
            mp[limit[i]].push_back(value[i]);
        }

        for (int i = 1; i <= n; i++) {  // top `i` with highest value for each limit
            sort(mp[i].begin(), mp[i].end());
            int use = 0;
            for (int j = mp[i].size() - 1; j >= 0; j--) {
                if (use >= i) break;
                total += mp[i][j];
                use++;
            }
        }
        return total;

    }
};
