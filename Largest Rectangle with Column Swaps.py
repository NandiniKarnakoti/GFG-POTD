# Problem: Largest Rectangle with Column Swaps
# Difficulty: Hard
# Date: 27 August 2026

"""
Problem:
Given a binary matrix, columns can be swapped any number
of times.

Return the maximum area of a rectangle consisting entirely
of 1s that can be formed after performing column swaps.
"""

# ---------------------------------------------------
# Approach: Histogram Heights + Sorting
# Time Complexity: O(N * M log M)
# Space Complexity: O(M)
# ---------------------------------------------------

class Solution:
    def maxArea(self, mat: list[list[int]]) -> int:
        # code here
        n = len(mat)
        m = len(mat[0])
        heights = [0] * m
        max_area = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            sorted_heights = sorted(heights, reverse=True)
            for j in range(m):
                max_area = max(max_area, sorted_heights[j] * (j + 1))
        return max_area
