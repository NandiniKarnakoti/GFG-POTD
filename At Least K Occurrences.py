# Problem: At Least K Occurrences
# Difficulty: Easy
# Date: 10 November 2026

"""
Problem:
Given an array arr[] and an integer k, find the first element
whose frequency reaches at least k.

If multiple elements qualify, return the one whose k-th
occurrence appears earliest. Return -1 if none qualifies.
"""

# ---------------------------------------------------
# Approach: Hash Map + Frequency Counting
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def firstElementKTime(self, arr: list[int], k: int) -> int:
        # code here
        freq={}
        for i in arr:
            freq[i]=freq.get(i,0)+1
            if freq[i]==k:
                return i
        return -1
