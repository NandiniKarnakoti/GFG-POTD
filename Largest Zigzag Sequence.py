# Problem: Largest Zigzag Sequence
# Difficulty: Easy
# Date: 9 August 2026

"""
Problem:
Given an n x n matrix, select one element from each row
such that two consecutive elements are not from the same
column.

Find the maximum possible sum.
"""

# ---------------------------------------------------
# Approach: Dynamic Programming
# Time Complexity: O(N²)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def zigzagSequence(self, mat):
        # code here
        n = len(mat)
        dp = mat[0][:]
        for i in range(1, n):
            max1 = -1
            max2 = -1
            max1_idx = -1

            for j in range(n):
                if dp[j] > max1:
                    max2 = max1
                    max1 = dp[j]
                    max1_idx = j
                elif dp[j] > max2:
                    max2 = dp[j]

            new_dp = [0] * n
            for j in range(n):
                if j == max1_idx:
                    new_dp[j] = mat[i][j] + max2
                else:
                    new_dp[j] = mat[i][j] + max1

            dp = new_dp

        return max(dp)
        
