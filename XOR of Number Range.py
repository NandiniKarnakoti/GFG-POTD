# Problem: XOR of Number Range
# Difficulty: Easy
# Date: 18 November 2026

"""
Problem:
Given two integers l and r, find the bitwise XOR
of all integers in the inclusive range [l, r].
"""

# ---------------------------------------------------
# Approach: Mathematical Observation + Bitwise XOR
# Time Complexity: O(1)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def findXOR(self, l: int, r: int) -> int:
        # code here
        def fun(n):
            if n%4==0:
                return n
            if n%4==1:
                return 1
            if n%4==2:
                return n+1
            return 0
        return fun(r)^fun(l-1)
