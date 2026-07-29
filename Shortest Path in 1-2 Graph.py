# Problem: Shortest Path in 1-2 Graph
# Difficulty: Hard
# Date: 29 July 2026

"""
Problem:
Given an undirected graph with edge weights
only 1 or 2, find the shortest distance
between the source and destination vertices.
Return -1 if the destination is unreachable.
"""

# ---------------------------------------------------
# Approach: Dijkstra's Algorithm
# Time Complexity: O((V + E) log V)
# Space Complexity: O(V + E)
# ---------------------------------------------------

class Solution:
    def shortestPath(self, V: int, src: int, dest: int, edges: list[list[int]]) -> int:
        # code here
        from heapq import heappush, heappop
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        INF = float('inf')
        dist = [INF] * V
        dist[src] = 0
        pq = [(0, src)]
        while pq:
            d, u = heappop(pq)
            if d > dist[u]:
                continue
            if u == dest:
                return d
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heappush(pq, (nd, v))
        return -1
        
