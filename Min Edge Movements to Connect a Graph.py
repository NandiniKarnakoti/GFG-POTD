# Problem: Min Edge Movements to Connect a Graph
# Difficulty: Medium
# Date: 10 August 2026

"""
Problem:
Given an undirected graph, find the minimum number
of edge movements required to make the graph connected.

In one operation, an existing edge can be removed
and added between any two vertices.
"""

# ---------------------------------------------------
# Approach: DSU (Disjoint Set Union)
# Time Complexity: O(N + M * α(N))
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def minEdgesReq(self, n, edges):
        # code here
        parent = list(range(n))
        rank = [0] * n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a, b):
            pa = find(a)
            pb = find(b)
            if pa == pb:
                return False
            if rank[pa] < rank[pb]:
                pa, pb = pb, pa
            parent[pb] = pa
            if rank[pa] == rank[pb]:
                rank[pa] += 1
            return True
        if len(edges) < n - 1:
            return -1
        for u, v in edges:
            union(u, v)
        components = 0
        for i in range(n):
            if find(i) == i:
                components += 1
        return components - 1
