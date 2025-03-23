// https://leetcode.com/problems/properties-graph/description/
// Disjoint set + some constant optimization

#include <bits/stdc++.h>

using namespace std;


class DisjointSet {
public:
    vector<int> parent;
    vector<int> sz;

    DisjointSet(int n) {
        parent.resize(n);
        sz.resize(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            sz[i] = 1;
        }
    }

    int find(int node) { // with path compression
        if (parent[node] == node) // root
            return node;
        return parent[node] = find(parent[node]);
    }

    void join(int a, int b) { // with union by size
        int root_a = find(a);
        int root_b = find(b);
        if (root_a == root_b)
            return;
        // join the smaller to the larger
        if (sz[root_b] > sz[root_a])
            swap(root_a, root_b);
        parent[root_b] = root_a;
        sz[root_a] += sz[root_b];
    }

    bool connected(int x, int y) {
        return find(x) == find(y);
    }
};

class Solution {
public:
    int intersect(vector<int> &a, vector<int> &b) {
        // note: this can be optimized with bitset since all elements are small
        unordered_set<int> sa(a.begin(), a.end());
        unordered_set<int> sb(b.begin(), b.end());
        int total = 0;
        for (int num: sa)
            if (sb.find(num) != sb.end())
                total++;
        return total;
    }

    int numberOfComponents(vector<vector<int>> &properties, int k) {
        int n = properties.size();
        vector<vector<int>> graph(n, vector<int>());

        DisjointSet ds(n);
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (ds.connected(i, j))  // already connected, don't check again
                    continue;
                if (intersect(properties[i], properties[j]) >= k) {
                    graph[i].push_back(j);
                    graph[j].push_back(i);
                    ds.join(i, j);
                }
            }
        }

        unordered_set<int> groups;  // count components by counting roots
        for (int i = 0; i < n; i++)
            groups.insert(ds.find(i));
        return groups.size();
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);


    return 0;
}