# Problem: Min Edge Reversals for Path
# Difficulty: Medium
# Date: 17 September 2026

"""
Problem:
Given a directed graph, find the minimum number of edges that
must be reversed to create a path from src to dst.

Return -1 if no path can be created.
"""

# ---------------------------------------------------
# Approach: 0-1 BFS
# Time Complexity: O(N + M)
# Space Complexity: O(N + M)
# ---------------------------------------------------

class Solution:
    def minimumEdgeReversal(self, edges: list[list[int]], n: int, src: int, dst: int) -> int:
        # code here
        from collections import deque
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append((v, 0))
            graph[v].append((u, 1))
        dist = [float('inf')] * (n + 1)
        dist[src] = 0
        dq = deque([src])
        while dq:
            u = dq.popleft()
            for v, cost in graph[u]:
                if dist[u] + cost < dist[v]:
                    dist[v] = dist[u] + cost
                    if cost == 0:
                        dq.appendleft(v)
                    else:
                        dq.append(v)
        return -1 if dist[dst] == float('inf') else dist[dst]
