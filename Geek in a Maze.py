# Problem: Geek in a Maze
# Difficulty: Hard
# Date: 23 August 2026

"""
Problem:
Given a maze containing empty cells ('.') and obstacles ('#'),
find the number of distinct empty cells Geek can visit starting
from cell (r, c).

Geek can move:
- Up at most u times
- Down at most d times
- Left or right any number of times
"""

# ---------------------------------------------------
# Approach: 0-1 BFS
# Time Complexity: O(N * M)
# Space Complexity: O(N * M)
# ---------------------------------------------------

class Solution:
    def numberOfCells(self, r: int, c: int, u: int, d: int, mat: list[list[int]]) -> int:
        # code here
        from collections import deque
        n=len(mat)
        m=len(mat[0])
        if mat[r][c]=='#':
            return 0
        INF=float('inf')
        dist=[[INF]*m for _ in range(n)]
        dq=deque([(r,c)])
        dist[r][c]=0
        directions=[(0,-1,0),(0,1,0),(-1,0,1),(1,0,0)]
        while dq:
            x,y=dq.popleft()
            for dx,dy,cost in directions:
                nx=x+dx
                ny=y+dy
                if 0<=nx<n and 0<=ny<m and mat[nx][ny]=='.':
                    new_up=dist[x][y]+cost
                    new_down=new_up+nx-r
                    if new_up<=u and new_down<=d and dist[nx][ny]>new_up:
                        dist[nx][ny]=new_up
                        if cost==0:
                            dq.appendleft((nx,ny))
                        else:
                            dq.append((nx,ny))
        return sum(dist[i][j]!=INF for i in range(n) for j in range(m))
        
