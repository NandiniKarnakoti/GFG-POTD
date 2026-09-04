# Problem: Max Adjacent Diffs Sum with 1 Replacements
# Difficulty: Medium
# Date: 3 September 2026

"""
Problem:
Given an integer array arr[], we can replace any number of
elements with 1.

Find the maximum possible sum of absolute differences between
consecutive elements after the modifications.
"""

# ---------------------------------------------------
# Approach: Dynamic Programming
# Time Complexity: O(N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def maxDiffSum(self, arr):
        # code here
        n = len(arr)
        if n == 1:
            return 0
        keep = 0  
        one = 0   
        for i in range(1, n):
            new_keep = max(
                keep + abs(arr[i] - arr[i - 1]),
                one + abs(arr[i] - 1)
            )
            new_one = max(
                keep + abs(1 - arr[i - 1]),
                one
            )
            keep = new_keep
            one = new_one
        return max(keep, one)
        
