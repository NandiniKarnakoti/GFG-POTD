# Problem: Trace Path
# Difficulty: Easy
# Date: 24 October 2026

"""
Problem:
Given a grid with n rows and m columns and a string of movement
commands, determine whether there exists a starting cell from which
Geek can follow all commands without leaving the grid.
"""

# ---------------------------------------------------
# Approach: Track Movement Boundaries
# Time Complexity: O(N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def isPossible(self, n: int, m: int, s: str) -> bool:
        # code here
        x=y=0
        min_x=max_x=min_y=max_y=0
        for c in s:
            if c=='L':
                y-=1
            elif c=='R':
                y+=1
            elif c=='D':
                x-=1
            else:
                x+=1
            min_x=min(min_x,x)
            max_x=max(max_x,x)
            min_y=min(min_y,y)
            max_y=max(max_y,y)
        return max_x-min_x<n and max_y-min_y<m
        
