# Problem: Mountain Subarray Queries
# Difficulty: Medium
# Date: 18 July 2026
# Language: Python

"""
Problem:
Given an array and multiple queries, determine
whether each queried subarray is a mountain array.

A mountain array is first non-decreasing and then
non-increasing. Entirely non-decreasing or
non-increasing subarrays are also considered valid.
"""

# ---------------------------------------------------
# Approach: Preprocessing Increasing & Decreasing Ranges
# Time Complexity: O(N + Q)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def processQueries(self, arr, queries):
        # code here
        n = len(arr)
        inc = [0] * n
        dec = [0] * n
        inc[-1] = dec[-1] = n - 1
        for i in range(n - 2, -1, -1):
            if arr[i] <= arr[i + 1]:
                inc[i] = inc[i + 1]
            else:
                inc[i] = i
            if arr[i] >= arr[i + 1]:
                dec[i] = dec[i + 1]
            else:
                dec[i] = i
        ans = []
        for l, r in queries:
            peak = inc[l]
            ans.append(peak >= r or dec[peak] >= r)
        return ans
        
