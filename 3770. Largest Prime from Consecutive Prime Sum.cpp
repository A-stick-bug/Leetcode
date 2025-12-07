// https://leetcode.com/problems/largest-prime-from-consecutive-prime-sum
// Direct solution, sieve all primes less than n
// Note: this would be much more efficient if we sieve once and reuse for each test case
// TC: O(n*loglogn)
//
// Outline of alternate solution (no precomputation)
// - Generate first ~sqrt(n) primes such that they sum to something >=n
// - take prefix sum
// - find last element in prefix sum that is a prime
// - should be at most O(n), can probably improve bound with math of prime distributions

class Solution {
public:
    int largestPrime(int n) {
        vector<bool> p(n + 1, true);
        p[1] = false;
        p[0] = false;
        for (int i = 2; i <= floor(sqrt(n)); i++) {
            if (not p[i]) continue;
            for (int j = i * i; j <= n; j += i)
                p[j] = false;
        }

        int cur = 0;
        unordered_set<int> works;
        for (int i = 2; i <= n and cur <= n; i++) {
            if (p[i]) {
                cur += i;
                works.insert(cur);
            }
        }
        for (int i = n; i >= 0; i--) {
            if (p[i] and works.find(i) != works.end())
                return i;
        }
        return 0;
    }
};
