# Problem: Maximum Frequency with K Increments
# Difficulty: Medium
# Date: 8 October 2026

"""
Problem:
Given an integer array arr[] and an integer k, find the maximum possible
frequency of any element after performing at most k operations.

In each operation, one element can be incremented by 1.
"""

# ---------------------------------------------------
# Approach: Sorting + Sliding Window
# Time Complexity: O(N log N)
# Space Complexity: O(1) auxiliary space
# ---------------------------------------------------

class Solution:
    def maxFrequency(self, arr, k):
        # code here
        arr.sort()
        left = 0
        total = 0
        ans = 1
        for right in range(len(arr)):
            total += arr[right]
            while arr[right] * (right-left+1) - total > k:
                total -= arr[left]
                left += 1
            ans = max(ans, right-left+1)
        return ans
