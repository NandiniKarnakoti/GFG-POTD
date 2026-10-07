# Problem: Longest Increasing Path in Matrix
# Difficulty: Hard
# Date: 6 October 2026

"""
Problem:
Given a matrix, find the length of the longest path where values are
strictly increasing.

The path can start and end at any cell and can move only up, down,
left, or right. A cell cannot be visited more than once.
"""

# ---------------------------------------------------
# Approach: Topological Sort using Kahn's Algorithm
# Time Complexity: O(N * M)
# Space Complexity: O(N * M)
# ---------------------------------------------------

class Solution:
    def longIncPath(self, matrix, n, m):
        # code here
        from collections import deque
        n=len(matrix)
        m=len(matrix[0])
        indegree=[[0]*m for _ in range(n)]
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(n):
            for j in range(m):
                for di,dj in directions:
                    ni=i+di
                    nj=j+dj
                    if 0<=ni<n and 0<=nj<m and matrix[ni][nj]>matrix[i][j]:
                        indegree[ni][nj]+=1
        queue=deque()
        for i in range(n):
            for j in range(m):
                if indegree[i][j]==0:
                    queue.append((i,j))
        length=0
        while queue:
            size=len(queue)
            length+=1
            for _ in range(size):
                i,j=queue.popleft()
                for di,dj in directions:
                    ni=i+di
                    nj=j+dj
                    if 0<=ni<n and 0<=nj<m and matrix[ni][nj]>matrix[i][j]:
                        indegree[ni][nj]-=1
                        if indegree[ni][nj]==0:
                            queue.append((ni,nj))
        return length
