#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxContainers(int n, int w, int maxWeight) {
        return min(n * n, maxWeight / w);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);


    return 0;
}