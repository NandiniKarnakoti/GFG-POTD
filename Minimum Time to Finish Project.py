# Problem: Minimum Time to Finish Project
# Difficulty: Medium
# Date: 1 October 2026

"""
Problem:
Given the duration required to complete each module and the dependency
relationships between modules, find the minimum time required to complete
the entire project.

Multiple modules can be completed simultaneously if all their dependencies
are completed.

If the dependency graph contains a cycle, return -1.
"""

# ---------------------------------------------------
# Approach: Topological Sort + Longest Path in DAG
# Time Complexity: O(N + M)
# Space Complexity: O(N + M)
# ---------------------------------------------------

class Solution:
    def minTime(self, duration, dependencies):
        # code here
        from collections import deque
        n = len(duration)
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        for u, v in dependencies:
            graph[u].append(v)
            indegree[v] += 1
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        finish_time = duration[:]
        count = 0
        answer = 0
        while queue:
            u = queue.popleft()
            count += 1
            answer = max(answer, finish_time[u])
            for v in graph[u]:
                finish_time[v] = max(
                    finish_time[v],
                    finish_time[u] + duration[v]
                )
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        if count != n:
            return -1
        return answer
