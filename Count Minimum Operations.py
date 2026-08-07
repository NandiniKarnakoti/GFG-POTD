# Problem: Count Minimum Operations
# Difficulty: Medium
# Date: 7 August 2026

"""
Problem:
Given an array initially filled with zeros,
find the minimum number of operations required
to obtain the given array.

Allowed operations:
1. Increment any single element by 1.
2. Double all elements of the array.
"""

# ---------------------------------------------------
# Approach: Bit Manipulation
# Time Complexity: O(N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def countMinOperations(self, arr):
        # code here
        increments = 0
        doublings = 0
        for x in arr:
            increments += x.bit_count()          
            if x:
                doublings = max(doublings, x.bit_length() - 1)
        return increments + doublings
        
