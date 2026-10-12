# Problem: Sort Two Parts Sorted
# Difficulty: Easy
# Date: 11 October 2026

"""
Problem:
Given an integer array arr[] consisting of two individually sorted parts
separated by a break point, merge them into a single sorted array.

The break point can be anywhere, including at the beginning or end.
"""

# ---------------------------------------------------
# Approach: Built-in Sorting
# Time Complexity: O(N log N)
# Space Complexity: O(1) auxiliary space
# ---------------------------------------------------

class Solution:
    def mergeTwoParts(self, arr):
        # code here
        arr.sort()
        return arr
