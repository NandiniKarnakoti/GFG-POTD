# Problem: Any Duplicate Within K Distance
# Difficulty: Easy
# Date: 11 November 2026

"""
Problem:
Given an array arr[] and an integer k, check whether
two distinct indices contain the same element and their
absolute difference is at most k.
"""

# ---------------------------------------------------
# Approach: Hash Map + Last Seen Index
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def checkWithinK(self, arr: list[int], k: int) -> bool:
        # code here
        seen={}
        for i in range(len(arr)):
            if arr[i] in seen and i-seen[arr[i]]<=k:
                return True
            seen[arr[i]]=i
        return False
