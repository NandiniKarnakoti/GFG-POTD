# Problem: Minimum Cost Selection
# Difficulty: Medium
# Date: 28 August 2026

"""
Problem:
Given an n x 3 matrix where each row contains the costs
of three choices, select exactly one choice from each row.

The same choice cannot be selected in two adjacent rows.

Return the minimum total cost required.
"""

# ---------------------------------------------------
# Approach: Dynamic Programming
# Time Complexity: O(N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def minCost(self, mat):
        """code here"""
        dp = mat[0][:]
        for i in range(1, len(mat)):
            new_dp = [0] * 3
            new_dp[0] = mat[i][0] + min(dp[1], dp[2])
            new_dp[1] = mat[i][1] + min(dp[0], dp[2])
            new_dp[2] = mat[i][2] + min(dp[0], dp[1])
            dp = new_dp
        return min(dp)
