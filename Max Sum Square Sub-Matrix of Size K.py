# Problem: Max Sum Square Sub-Matrix of Size K
# Difficulty: Medium
# Date: 26 July 2026
# Language: Python

"""
Problem:
Given an n × n matrix and an integer k,
find the maximum sum among all possible
k × k square sub-matrices.
"""

# ---------------------------------------------------
# Approach: 2D Prefix Sum
# Time Complexity: O(N²)
# Space Complexity: O(N²)
# ---------------------------------------------------

class Solution:
    def maximumSum(self, mat, k):
        # code here
        n = len(mat)
        prefix = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    mat[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )
        ans = float("-inf")
        for i in range(n - k + 1):
            for j in range(n - k + 1):
                total = (
                    prefix[i + k][j + k]
                    - prefix[i][j + k]
                    - prefix[i + k][j]
                    + prefix[i][j]
                )
                ans = max(ans, total)
        return ans
        
