# Problem: Min Steps by Knight
# Difficulty: Medium
# Date: 29 September 2026

"""
Problem:
Given an n x n chessboard and the initial and target positions
of a Knight, find the minimum number of moves required to reach
the target position.

The Knight can move in 8 possible L-shaped directions.
Positions are given using 1-based indexing.
"""

# ---------------------------------------------------
# Approach: Breadth-First Search (BFS)
# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
# ---------------------------------------------------

class Solution:
	def minStepToReachTarget(self, knightPos: list[int], targetPos: list[int], n: int) -> int:
		#Code here
        from collections import deque
        start_x, start_y = knightPos
        target_x, target_y = targetPos
        moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        visited = [[False] * (n + 1) for _ in range(n + 1)]
        queue = deque()
        queue.append((start_x, start_y, 0))
        visited[start_x][start_y] = True
        while queue:
            x, y, dist = queue.popleft()
            if x == target_x and y == target_y:
                return dist
            for dx, dy in moves:
                new_x = x + dx
                new_y = y + dy
                if 1 <= new_x <= n and 1 <= new_y <= n and not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y, dist + 1))
        return -1
