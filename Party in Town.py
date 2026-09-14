# Problem: Party in Town
# Difficulty: Medium
# Date: 13 September 2026

"""
Problem:
Given a tree representing n houses connected by n - 1 roads,
choose a house such that its maximum distance from any other
house is minimized.

Return the minimum possible maximum distance.
"""

# ---------------------------------------------------
# Approach: Two BFS Traversals + Tree Diameter
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def partyHouse(self, adj: list[list[int]]) -> int:
        # code here
        from collections import deque
        n = len(adj)
        def bfs(start):
            dist = [-1] * n
            dist[start] = 0
            q = deque([start])
            farthest = start
            while q:
                u = q.popleft()
                for v in adj[u]:
                    v -= 1
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
                        if dist[v] > dist[farthest]:
                            farthest = v
            return farthest, dist[farthest]
        a, _ = bfs(0)
        b, diameter = bfs(a)
        return (diameter + 1) // 2
