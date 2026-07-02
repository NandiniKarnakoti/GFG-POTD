# Problem: Max Subarray Sum by Removing At Most One 
# Difficulty: Medium 
# Date: 1 July 2026

""" 
Problem:
Find the maximum subarray sum where at most one 
element can be removed.

The resulting subarray must remain non-empty.
"""

# --------------------------------------------------- 
# Approach: Dynamic Programming (Modified Kadane) 
# Time Complexity: O(N) 
# Space Complexity: O(1) 
# ---------------------------------------------------

class Solution:
    def maxSumSubarray(self, arr):
        # code here
        n = len(arr)
        no_del = arr[0]      
        one_del = float('-inf')  
        ans = arr[0]
        for i in range(1, n):
            new_one_del = max(one_del + arr[i], no_del)
            new_no_del = max(arr[i], no_del + arr[i])
            one_del = new_one_del
            no_del = new_no_del
            ans = max(ans, no_del, one_del)
        return ans
