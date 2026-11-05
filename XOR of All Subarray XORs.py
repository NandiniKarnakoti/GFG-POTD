# Problem: XOR of All Subarray XORs
# Difficulty: Medium
# Date: 4 November 2026

"""
Problem:
Given an integer array arr[], find the XOR of XOR values
of all possible non-empty subarrays.
"""

# ---------------------------------------------------
# Approach: Mathematical Observation + Bitwise XOR
# Time Complexity: O(N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def subarrayXor(self, arr):
        # code here 
        n=len(arr)
        res=0
        for i in range(n):
            c=(i+1)*(n-i)
            if c%2==1:
                res^=arr[i]
        return res
