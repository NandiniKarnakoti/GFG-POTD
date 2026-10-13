# Problem: Minimum Squares with Full Cuts
# Difficulty: Medium
# Date: 12 October 2026

"""
Problem:
Given a rectangular paper of dimensions n x m, find the minimum number
of squares that can be formed by cutting completely across the remaining
paper, either horizontally or vertically.
"""

# ---------------------------------------------------
# Approach: Greedy + Euclidean Algorithm
# Time Complexity: O(log(min(N, M)))
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def minSquares(self, n, m):
        # code here
        c=0
        while n>0 and m>0:
            if n<m:
                n,m=m,n
            c+=n//m
            n%=m
        return c
        
