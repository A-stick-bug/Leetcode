class Solution {
public:
    int earliestTime(vector<vector<int>>& tasks) {
        int best = 9999;
        for (auto x: tasks) {
            best = min(best, x[0]+x[1]);
        }
        return best;
    }
};