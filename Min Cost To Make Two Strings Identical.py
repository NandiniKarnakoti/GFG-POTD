# Problem: Min Cost To Make Two Strings Identical
# Difficulty: Medium
# Date: 19 September 2026

"""
Problem:
Given two strings s1 and s2 and the costs of deleting a character
from each string, find the minimum cost required to make both
strings identical.

Characters can be deleted from either string, but the order of
the remaining characters must be preserved.
"""

# ---------------------------------------------------
# Approach: Dynamic Programming
# Time Complexity: O(N * M)
# Space Complexity: O(N * M)
# ---------------------------------------------------

class Solution:
    def findMinCost(self, s1: str, s2: str, costS1: int, costS2: int) -> int:
        # code here
        n = len(s1)
        m = len(s2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][0] = i * costS1
        for j in range(1, m + 1):
            dp[0][j] = j * costS2
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    delete_s1 = dp[i - 1][j] + costS1
                    delete_s2 = dp[i][j - 1] + costS2
                    dp[i][j] = min(delete_s1, delete_s2)
        return dp[n][m]
