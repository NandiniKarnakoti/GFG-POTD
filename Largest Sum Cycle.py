# Problem: Largest Sum Cycle
# Difficulty: Hard
# Date: 2 November 2026

"""
Problem:
Given an array edge[] representing a directed graph where each
node has at most one outgoing edge, find the maximum sum of
node indices belonging to any cycle.

Return -1 if no cycle exists.
"""

# ---------------------------------------------------
# Approach: Graph Traversal + Cycle Detection
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def largestSumCycle(self, edge):
        # code here
        n=len(edge)
        visited=[False]*n
        max_sum=-1
        for i in range(n):
            if visited[i]:
                continue
            current=i
            path=[]
            position={}
            while current!=-1 and not visited[current]:
                visited[current]=True
                position[current]=len(path)
                path.append(current)
                current=edge[current]
            if current!=-1 and current in position:
                cycle=path[position[current]:]
                cycle_sum=sum(cycle)
                max_sum=max(max_sum,cycle_sum)
        return max_sum
