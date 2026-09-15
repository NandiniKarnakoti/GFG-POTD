# Problem: Shortest Safe Route in Grid
# Difficulty: Medium
# Date: 14 September 2026

"""
Problem:
Given a matrix containing safe cells (1) and landmines (0),
find the minimum number of steps required to travel from any
cell in the leftmost column to any cell in the rightmost column.

A cell is unsafe if it contains a landmine or is directly adjacent
to a landmine. Unsafe cells cannot be used.

Return -1 if no safe path exists.
"""

# ---------------------------------------------------
# Approach: Mark Unsafe Cells + BFS
# Time Complexity: O(N * M)
# Space Complexity: O(N * M)
# ---------------------------------------------------

class Solution:
    def shortestPath(self, mat: list[list[int]]) -> int:
        # code here
        from collections import deque
        n = len(mat)
        m = len(mat[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        safe = [row[:] for row in mat]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    safe[i][j] = 0
                    for di,dj in directions:
                        ni,nj = i+di,j+dj
                        if 0 <= ni < n and 0 <= nj < m:
                            safe[ni][nj] = 0
        q = deque()
        for i in range(n):
            if safe[i][0] == 1:
                q.append((i,0,1))
                safe[i][0] = 0
        while q:
            r,c,dist = q.popleft()
            if c == m-1:
                return dist
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if 0 <= nr < n and 0 <= nc < m and safe[nr][nc] == 1:
                    safe[nr][nc] = 0
                    q.append((nr,nc,dist+1))
        return -1
