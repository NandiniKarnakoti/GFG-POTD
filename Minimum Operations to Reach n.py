# Problem: Minimum Operations to Reach n
# Difficulty: Easy
# Date: 9 October 2026

"""
Problem:
Given a number n, find the minimum number of operations required to
reach n starting from 0.

The two allowed operations are:
1. Double the current number.
2. Add 1 to the current number.
"""

# ---------------------------------------------------
# Approach: Greedy + Reverse Operations
# Time Complexity: O(log N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def minOperation(self, n):
        # code here
        c=0
        while n>0:
            if n%2==0:
                n=n//2
            else:
                n=n-1
            c+=1
        return c
