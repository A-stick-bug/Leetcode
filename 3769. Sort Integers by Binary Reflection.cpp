// https://leetcode.com/problems/sort-integers-by-binary-reflection
// Custom comparator + bitwise

class Solution {
public:
    static int rev(int n) {
        int res = 0;
        int le = 32 - __builtin_clz(n);
        for (int bit = 0; bit < le; bit++) {
            if (n & (1 << bit)) {
                res += (1 << (le - bit - 1));
            }
        }
        //cout << n << " " << res << "\n";
        return res;
    }
    static bool comp(int a, int b) {
        if (rev(a) == rev(b)) return a < b;
        return rev(a) < rev(b);
    }
    vector<int> sortByReflection(vector<int>& nums) {
        stable_sort(nums.begin(), nums.end(), comp);
        return nums;
    }
};
