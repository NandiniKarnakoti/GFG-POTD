# Problem: Longest Path in a Directed Acyclic Graph
# Difficulty: Hard
# Date: 13 August 2026

"""
Problem:
Given a weighted DAG and a source vertex src,
find the longest distance from src to every vertex.

If a vertex is unreachable from src, store INT_MIN.
"""

# ---------------------------------------------------
# Approach: Topological Sort + Dynamic Programming
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
# ---------------------------------------------------

class Solution:
    def maxDistance(self, V, src, edges):
        # code here
        from collections import deque
        adj=[[] for _ in range(V)]
        indegree=[0]*V
        for u,v,w in edges:
            adj[u].append((v,w))
            indegree[v]+=1
        q=deque()
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        topo=[]
        while q:
            u=q.popleft()
            topo.append(u)
            for v,w in adj[u]:
                indegree[v]-=1
                if indegree[v]==0:
                    q.append(v)
        dist=[-2**31]*V
        dist[src]=0
        for u in topo:
            if dist[u]==-2**31:
                continue
            for v,w in adj[u]:
                dist[v]=max(dist[v],dist[u]+w)
        return dist
 

