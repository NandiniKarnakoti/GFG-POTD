# Problem: Longest Bitonic Subarray
# Difficulty: Medium
# Date: 15 July 2026

"""
Problem:
Find the maximum length of a bitonic subarray.

A bitonic subarray first monotonically increases
and then monotonically decreases.
"""

# ---------------------------------------------------
# Approach: Prefix Increasing + Suffix Decreasing
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
	def bitonic(self,arr):
		# code here
		n = len(arr)
        inc = [1] * n
        for i in range(1, n):
            if arr[i] >= arr[i - 1]:
                inc[i] = inc[i - 1] + 1
        dec = [1] * n
        for i in range(n - 2, -1, -1):
            if arr[i] >= arr[i + 1]:
                dec[i] = dec[i + 1] + 1
        ans = 1
        for i in range(n):
            ans = max(ans, inc[i] + dec[i] - 1)
        return ans
