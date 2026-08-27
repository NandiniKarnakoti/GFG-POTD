# Problem: Negative Weight Cycle
# Difficulty: Medium
# Date: 26 August 2026

"""
Problem:
Given a weighted directed graph, determine whether
the graph contains a negative weight cycle.
"""

# ---------------------------------------------------
# Approach: Bellman-Ford Algorithm
# Time Complexity: O(V * E)
# Space Complexity: O(V)
# ---------------------------------------------------

class Solution:
    def isNegativeWeightCycle(self, V: int, edges: list[list[int]]) -> bool:
        # code here
        dist = [0] * V
        for _ in range(V - 1):
            for u, v, w in edges:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                return True
        return False
