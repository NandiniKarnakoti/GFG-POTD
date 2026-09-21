# Problem: Largest Subsquare Surrounded by X
# Difficulty: Medium
# Date: 20 September 2026

"""
Problem:
Given an n x n matrix containing 'X' and 'O', find the largest
square submatrix whose four boundaries are completely surrounded
by 'X'.

The cells inside the square can contain either 'X' or 'O'.
"""

# ---------------------------------------------------
# Approach: Precompute Right and Down X Counts
# Time Complexity: O(N^3)
# Space Complexity: O(N^2)
# ---------------------------------------------------

class Solution:
    def largestSubsquare(self, mat):
        # code here
        n = len(mat)
        right = [[0] * (n + 1) for _ in range(n)]
        down = [[0] * n for _ in range(n + 1)]
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 'X':
                    right[i][j] = right[i][j + 1] + 1
                    down[i][j] = down[i + 1][j] + 1
        for i in range(n):
            for j in range(n):
                if mat[i][j] == 'X':
                    size = min(right[i][j], down[i][j])
                    while size > ans:
                        if right[i + size - 1][j] >= size and down[i][j + size - 1] >= size:
                            ans = size
                            break
                        size -= 1
        return ans
