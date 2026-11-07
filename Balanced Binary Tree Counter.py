# Problem: Balanced Binary Tree Counter
# Difficulty: Easy
# Date: 6 November 2026

"""
Problem:
Given a height h, find the maximum number of distinct
balanced binary trees of height exactly h.

Return the count modulo 10^9 + 7.
"""

# ---------------------------------------------------
# Approach: Space-Optimized Dynamic Programming
# Time Complexity: O(H)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def countBT(self, h: int) -> int:
        # code here
        mod=10**9+7
        if h==1:
            return 1
        if h==2:
            return 3
        a=1
        b=3
        for i in range(3,h+1):
            c=(b*b+2*b*a)%mod
            a=b
            b=c
        return b
