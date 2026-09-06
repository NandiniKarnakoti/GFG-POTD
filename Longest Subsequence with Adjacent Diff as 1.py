# Problem: Longest Subsequence with Adjacent Diff as 1
# Difficulty: Medium
# Language: Python

"""
Problem:
Given an array arr[], find the longest subsequence such that
the absolute difference between every pair of adjacent elements
in the subsequence is exactly 1.
"""

# ---------------------------------------------------
# Approach: Dynamic Programming with Hash Map
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def longestSubseq(self, arr):
        # code here
        dp = {}
        ans = 0
        for x in arr:
            prev = max(dp.get(x - 1, 0), dp.get(x + 1, 0))
            dp[x] = max(dp.get(x, 0), prev + 1)
            ans = max(ans, dp[x])
        return ans
