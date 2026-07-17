# GeeksForGeeks POTD
# Problem: Numbers with Given Digit Sum
# Difficulty: Medium
# Date: 16 July 2026
# Language: Python

"""
Problem:
Count the number of n-digit positive integers
whose digits add up to the given sum.

Return -1 if no such number exists.
"""

# ---------------------------------------------------
# Approach: Dynamic Programming
# Time Complexity: O(N × Sum × 10)
# Space Complexity: O(N × Sum)
# ---------------------------------------------------


class Solution:
    def countWays(self, n, sum):
        # code here
        dp = [[0] * (sum + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for s in range(sum + 1):
                start = 1 if i == 1 else 0
                for d in range(start, 10):
                    if s >= d:
                        dp[i][s] += dp[i - 1][s - d]
        return dp[n][sum] if dp[n][sum] else -1
