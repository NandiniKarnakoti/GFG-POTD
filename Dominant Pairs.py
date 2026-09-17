# Problem: Dominant Pairs
# Difficulty: Easy
# Date: 16 September 2026

"""
Problem:
Given an even-sized integer array arr[], count the number of
dominant pairs (i, j) such that i belongs to the first half,
j belongs to the second half, and:

arr[i] >= 5 * arr[j]
"""

# ---------------------------------------------------
# Approach: Binary Search
# Time Complexity: O(N log N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def dominantPairs(self, arr: list[int]) -> int:
        # code here
        from bisect import bisect_right
        n = len(arr)
        mid = n // 2
        right = sorted(arr[mid:])
        ans = 0
        for x in arr[:mid]:
            ans += bisect_right(right, x // 5)
        return ans
    
