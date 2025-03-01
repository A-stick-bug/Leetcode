class Solution {
public:
    int countArrays(vector<int> &original, vector <vector<int>> &bounds) {
        int n = original.size();
        for (int i = 0; i < n; i++) {
            bounds[i][0] -= original[i];
            bounds[i][1] -= original[i];
        }

        int low = -(1 << 30);
        int high = 1 << 30;
        for (int i = 0; i < n; i++) {
            low = max(low, bounds[i][0]);
            high = min(high, bounds[i][1]);
        }
        return max(0, high - low + 1);
    }
};
