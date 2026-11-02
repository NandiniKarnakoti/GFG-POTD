# Problem: Maximum Subarray Sum with One Square Allowed
# Difficulty: Medium
# Date: 1 November 2026

"""
Problem:
Given an integer array arr[], find the maximum subarray sum
by squaring at most one element.
"""

# ---------------------------------------------------
# Approach: Modified Kadane's Algorithm (Two States)
# Time Complexity: O(N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def maximumSubarray(self, arr: list[int]) -> int:
        """ code here """
        normal=arr[0]
        squared=arr[0]*arr[0]
        ans=squared
        for x in arr[1:]:
            squared=max(x*x,normal+x*x,squared+x)
            normal=max(x,normal+x)
            ans=max(ans,normal,squared)
        return ans
