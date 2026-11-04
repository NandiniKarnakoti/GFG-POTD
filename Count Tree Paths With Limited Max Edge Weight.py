# Problem: Count Tree Paths With Limited Max Edge Weight
# Difficulty: Hard
# Date: 3 November 2026

"""
Problem:
Given a weighted tree and queries representing maximum
allowed edge weights, count the number of distinct paths
whose every edge weight is less than or equal to each query.

Paths are undirected, and paths containing zero edges
are not considered.
"""

# ---------------------------------------------------
# Approach: DSU (Union-Find) + Offline Sorting
# Time Complexity: O((N + Q) * α(N) + N log N + Q log Q)
# Space Complexity: O(N + Q)
# ---------------------------------------------------

class Solution:
    def maximumWeight(self, n, edges, queries):
        # code here
        parent=list(range(n+1))
        size=[1]*(n+1)
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(u,v):
            ru=find(u)
            rv=find(v)
            if ru==rv:
                return 0
            pairs=size[ru]*size[rv]
            if size[ru]<size[rv]:
                ru,rv=rv,ru
            parent[rv]=ru
            size[ru]+=size[rv]
            return pairs
        edges.sort(key=lambda x:x[2])
        sorted_queries=sorted(enumerate(queries),key=lambda x:x[1])
        ans=[0]*len(queries)
        total=0
        j=0
        for idx,q in sorted_queries:
            while j<len(edges) and edges[j][2]<=q:
                u,v,w=edges[j]
                total+=union(u,v)
                j+=1
            ans[idx]=total
        return ans
