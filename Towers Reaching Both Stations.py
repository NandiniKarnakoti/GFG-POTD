# Problem: Towers Reaching Both Stations 
# Difficulty: Medium 
# Date: 7 July 2026

""" 
Problem:
Count the number of towers from which a signal
can reach both control stations.

Station P: Top row and Left column
Station Q: Bottom row and Right column 
"""

# --------------------------------------------------- 
# Approach: Multi-Source BFS 
# Time Complexity: O(N × M) 
# Space Complexity: O(N × M) 
# ---------------------------------------------------

class Solution:
    def countCoordinates(self, mat):
        # code here
        from collections import deque
        n = len(mat)
        m = len(mat[0])
        def bfs(starts):
            vis = [[False] * m for _ in range(n)]
            q = deque()
            for x, y in starts:
                if not vis[x][y]:
                    vis[x][y] = True
                    q.append((x, y))
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while q:
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < n and 0 <= ny < m and
                        not vis[nx][ny] and
                        mat[nx][ny] >= mat[x][y]):
                        vis[nx][ny] = True
                        q.append((nx, ny))
            return vis
        pacific = []
        atlantic = []
        for i in range(n):
            pacific.append((i, 0))
            atlantic.append((i, m - 1))
        for j in range(m):
            pacific.append((0, j))
            atlantic.append((n - 1, j))
        p = bfs(pacific)
        q = bfs(atlantic)
        ans = 0
        for i in range(n):
            for j in range(m):
                if p[i][j] and q[i][j]:
                    ans += 1
        return ans
        
