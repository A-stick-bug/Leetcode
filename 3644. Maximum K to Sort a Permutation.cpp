// https://leetcode.com/problems/maximum-k-to-sort-a-permutation
// Bitwise AND of all elements in incorrect position is the answer
// The observation isn't that intuitive
//
// Reasoning steps:
// - We pick `K` which must be able to swap with anything not yet in their correct positions
// - Note that K = 0 always works since 0 AND `x` is 0
// - Since we want to maximize K, we just pick the largest number that can swap with anything

class Solution {
public:
    int sortPermutation(vector<int>& nums) {
        int n = nums.size();

        int first = -1;
        for (int i = 0; i < n; i++) {
            if (nums[i] != i) {
                first = i;
                break;
            }
        }

        if (first == -1) {  // already sorted
            return 0;
        }

        int cur = (1 << 29) - 1;
        for (int i = 0; i < n; i++) {
            if (nums[i] != i) {
                cur &= nums[i];
            }
        }
        return cur;
    }
};