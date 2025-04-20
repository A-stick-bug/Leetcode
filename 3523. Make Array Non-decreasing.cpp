// https://leetcode.com/problems/make-array-non-decreasing
// Observation based question, simplifies to prefix max
//
// Login behind code:
// - start with the first number and loop to the right
// - for any number smaller than it, we must combine it with the first one to keep it non-decreasing
// - for any number >= cur, we can now treat it as the new start and repeat

#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    int maximumPossibleSize(vector<int>& nums) {
        int total = 0;
        int pref_max = 0;
        for (int num: nums) {
            if (num >= pref_max) {
                pref_max = num;
                total++;
            }
        }
        return total;
    }
};


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);



    return 0;
}