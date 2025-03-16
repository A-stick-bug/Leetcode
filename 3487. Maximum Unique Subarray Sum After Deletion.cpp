#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxSum(vector<int> &nums) {
        unordered_set<int> vis;
        int total = 0;
        int found = false;
        for (int num: nums) {
            if (vis.find(num) != vis.end())
                continue;
            if (num <= 0)
                continue;
            total += num;
            vis.insert(num);
            found = true;
        }
        if (found)
            return total;
        else
            return *max_element(nums.begin(), nums.end());
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);


    return 0;
}