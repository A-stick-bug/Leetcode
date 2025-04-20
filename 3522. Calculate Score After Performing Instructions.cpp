#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    long long calculateScore(vector<string>& instructions, vector<int>& values) {
        int n = values.size();
        vector<bool> vis(n);
        long long score = 0;
        int idx = 0;
        while (0 <= idx and idx < n and not vis[idx]) {
            vis[idx] = true;
            if (instructions[idx] == "add") {
                score += values[idx];
                idx++;
            }
            else {
                idx += values[idx];
            }
        }
        return score;
    }
};


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);



    return 0;
}