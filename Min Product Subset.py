# Problem: Min Product Subset
# Difficulty: Medium
# Date: 16 August 2026

"""
Problem:
Given an integer array, find the minimum product
that can be obtained from any non-empty subset.
"""

# ---------------------------------------------------
# Approach: Bitmask / Subset Enumeration
# Time Complexity: O(2^N × N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def minProd(self, arr):
        # code here
        n=len(arr)
        res=float('inf')
        for m in range(1,1<<n):
            product=1
            for i in range(n):
                if m & (1<<i):
                    product*=arr[i]
            res=min(res,product)
        return res
