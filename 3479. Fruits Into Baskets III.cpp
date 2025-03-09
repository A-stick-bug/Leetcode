// https://leetcode.com/problems/fruits-into-baskets-iii
// Basically optimize the brute force with data structures
// Segment tree + binary search to find first index with value >= val`
// TC: O(n * log^2(n))

#include <bits/stdc++.h>

using namespace std;

class SegTree {
    vector<int> seg;
    function<int(int, int)> f;
    int default_val, N;

public:
    SegTree(vector<int> &arr, function<int(int, int)> f, int default_val) : f(f), default_val(default_val) {
        int layers = ceil(log2(arr.size()));
        N = 1 << layers;
        seg.resize(N << 1, default_val);
        for (size_t i = 0; i < arr.size(); ++i)
            seg[i + N] = arr[i];
        for (int i = N - 1; i > 0; --i)
            seg[i] = f(seg[i << 1], seg[(i << 1) | 1]);
    }

    void update(int i, int val) {
        for (seg[i += N] = val; i > 1; i >>= 1)
            seg[i >> 1] = f(seg[i], seg[i ^ 1]);
    }

    int query(int l, int r) {
        int resl = default_val, resr = default_val;
        for (l += N, r += N; l <= r; l >>= 1, r >>= 1) {
            if (l & 1) resl = f(resl, seg[l++]);
            if (!(r & 1)) resr = f(seg[r--], resr);
        }
        return f(resl, resr);
    }
};

int mx(int a, int b) {  // functions for the segment tree
    return max(a, b);
}

class Solution {
public:
    int numOfUnplacedFruits(vector<int> &fruits, vector<int> &baskets) {
        SegTree seg(baskets, mx, 0);
        int n = fruits.size();

        int skipped = 0;
        for (auto val: fruits) {
            if (seg.query(0, n - 1) < val) {  // none available
                skipped += 1;
                continue;
            }

            int low = 0;
            int high = n - 1;
            int ans = n - 1;
            while (low <= high) {
                int mid = (low + high) / 2;
                if (seg.query(0, mid) >= val) {
                    ans = mid;
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
            seg.update(ans, -1);
        }
        return skipped;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);


    return 0;
}