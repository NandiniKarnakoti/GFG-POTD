# Problem: Longest Possible Route in a Matrix with Hurdles
# Difficulty: Medium
# Date: 11 July 2026

"""
Problem:
Find the length of the longest path from
source to destination in a binary matrix.

A cell can be visited at most once.
0 represents a blocked cell.
"""

# ---------------------------------------------------
# Approach: Backtracking (DFS)
# Time Complexity: O(4^(N*M)) in the worst case
# Space Complexity: O(N*M)
# ---------------------------------------------------

class Solution:
    def longestPath(self, mat, xs, ys, xd, yd):
        # code here
        m = len(mat[0])
        if mat[xs][ys] == 0 or mat[xd][yd] == 0:
            return -1
        visited = [[False] * m for _ in range(n)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(x, y):
            if x == xd and y == yd:
                return 0
            visited[x][y] = True
            ans = -1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (0 <= nx < n and 0 <= ny < m and
                        mat[nx][ny] == 1 and
                        not visited[nx][ny]):
                    res = dfs(nx, ny)
                    if res != -1:
                        ans = max(ans, res + 1)
            visited[x][y] = False
            return ans
        return dfs(xs, ys)
