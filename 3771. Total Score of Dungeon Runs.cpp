// https://leetcode.com/problems/total-score-of-dungeon-runs
// Maintain current HP for all starting days simultaneously
//
// Data structure based solution, but optimized
// Inspiration: first note that segment tree trivializes the problem
// - simply range update to decrease HP, tree walk (traversal) to count number >req[i]
//
// Notice how the range updates is always on all current elements
// We maintain an offset such that the true HP is cur[i]+offset
// When adding a new element to cur, we must counter the offset of previous updates as they do not apply to it
// Next, note that cur is monotonic decreasing (HP only decreases), allowing us to binary search
//
// TC: O(nlogn)

#define ll long long

class Solution {
public:
    long long totalScore(int hp, vector<int>& damage, vector<int>& requirement) {
        int offset = 0;
        ll total = 0;
        vector<int> cur;  // monotonic increasing, cur[i] = hp starting at i+1
        int n = damage.size();

        for (int i = 0; i < n; i++) {
            cur.push_back(hp - offset);
            offset -= damage[i];  // damage all in cur

            int idx = lower_bound(cur.begin(), cur.end(), requirement[i] - offset) - cur.begin();
            //cout << idx << "\n";
            total += cur.size() - idx;
        }
        return total;
    }
};
