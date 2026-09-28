# Problem: Longest Colored Path
# Difficulty: Hard
# Date: 27 September 2026

"""
Problem:
Given a tree whose nodes are colored Red (R) or Blue (B),
find the longest path such that no Red node appears after a
Blue node.

A valid path can contain:
- Only Red nodes
- Only Blue nodes
- Red nodes followed by Blue nodes

A Blue -> Red transition is not allowed.
"""

# ---------------------------------------------------
# Approach: Same-Color Components + Tree Diameter
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def longestPath(self, s, edges):
        # code here
        n = len(s)
        g = [[] for _ in range(n)]
        for u, v in edges:
            u -= 1
            v -= 1
            g[u].append(v)
            g[v].append(u)
        comp = [-1] * n
        comps = []
        cid = 0
        for i in range(n):
            if comp[i] != -1:
                continue
            stack = [i]
            comp[i] = cid
            nodes = []
            while stack:
                u = stack.pop()
                nodes.append(u)
                for v in g[u]:
                    if comp[v] == -1 and s[v] == s[u]:
                        comp[v] = cid
                        stack.append(v)
            comps.append(nodes)
            cid += 1
        ecc = [0] * n
        for nodes in comps:
            start = nodes[0]
            def bfs(start):
                dist = {start: 0}
                stack = [(start, -1)]
                far = start
                while stack:
                    u, p = stack.pop()
                    if dist[u] > dist[far]:
                        far = u
                    for v in g[u]:
                        if v != p and s[v] == s[u]:
                            dist[v] = dist[u] + 1
                            stack.append((v, u))
                return far, dist
            a, _ = bfs(start)
            b, d1 = bfs(a)
            _, d2 = bfs(b)
            for u in nodes:
                ecc[u] = max(d1[u], d2[u])
        ans = 1
        for u, v in edges:
            u -= 1
            v -= 1
            if s[u] != s[v]:
                ans = max(ans, ecc[u] + ecc[v] + 2)
        for u in range(n):
            ans = max(ans, ecc[u] + 1)
        return ans
