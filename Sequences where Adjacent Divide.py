# Problem: Sequences where Adjacent Divide
# Difficulty: Medium
# Date: 3 August 2026
# Language: Python

"""
Problem:
Count the number of arrays of size n such that:

- Every element lies in the range [1, m].
- For every adjacent pair, one element divides
  the other.
"""

# ---------------------------------------------------
# Approach: Dynamic Programming
# Time Complexity: O(N × M²)
# Space Complexity: O(N × M)
# ---------------------------------------------------

class Solution:
    def count(self, n: int, m: int) -> int:
        # code here
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for j in range(1, m + 1):
            dp[1][j] = 1
        for length in range(2, n + 1):
            for j in range(1, m + 1):
                for k in range(1, m + 1):
                    if j % k == 0 or k % j == 0:
                        dp[length][j] += dp[length - 1][k]
        return sum(dp[n][1:])
