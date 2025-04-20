#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    string smallestPalindrome(string s) {
        unordered_map<char, int> freq;
        for (auto c: s) freq[c]++;

        string prefix = "";
        string middle = "";
        for (char c = 'a'; c <= 'z'; c++) {
            for (int i = 0; i < freq[c] / 2; i++) {
                prefix += c;
            }
            if (freq[c] % 2 == 1)
                middle += c;
        }

        string suffix = prefix;
        reverse(suffix.begin(), suffix.end());
        return prefix + middle + suffix;
    }
};


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);



    return 0;
}