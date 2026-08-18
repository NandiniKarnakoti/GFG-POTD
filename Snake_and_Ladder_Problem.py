# GeeksForGeeks POTD
# Problem: Snake and Ladder Problem
# Difficulty: Medium
# Date: 17 August 2026

"""
Problem:
Given an n x n Snakes and Ladders board, find the minimum
number of dice throws required to reach cell n*n starting
from cell 1.

lad contains ladder start/end positions.
sn contains snake start/end positions.
"""

# ---------------------------------------------------
# Approach: BFS
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------
class Solution:
    def minThrows(self, n, lad, sn):
        # code here
        from collections import deque
        N=n*n
        jump=[-1]*(N+1)
        for i in range(0,len(lad),2):
            jump[lad[i]]=lad[i+1]
        for i in range(0,len(sn),2):
            jump[sn[i]]=sn[i+1]
        q=deque([1])
        visited=[False]*(N+1)
        visited[1]=True
        throws=0
        while q:
            for _ in range(len(q)):
                cell=q.popleft()
                for dice in range(1,7):
                    nxt=cell+dice
                    if nxt>N:
                        continue
                    if jump[nxt]!=-1:
                        nxt=jump[nxt]
                    if nxt==N:
                        return throws+1
                    if not visited[nxt]:
                        visited[nxt]=True
                        q.append(nxt)
            throws+=1
        return -1
        
