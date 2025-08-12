// https://leetcode.com/problems/flip-square-submatrix-vertically/
// Simple implementation

class Solution {
public:
    vector<vector<int>> reverseSubmatrix(vector<vector<int>>& grid, int x, int y, int k) {
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<int>> ans(n, vector<int>(m));

        int xx = x + k - 1;
        int yy = y + k - 1;
        for (int i = 0; i < k/2; i++) {
            for (int j = 0; j < k; j++) {
                swap(grid[i+x][y+j], grid[xx-i][y+j]);
            }
        }
        return grid;
    }
};
