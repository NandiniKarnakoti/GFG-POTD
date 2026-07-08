# Problem: Largest Unblocked Submatrix 
# Difficulty: Medium 
# Date: 7 July 2026

""" 
Problem: 
Given blocked cells, where each blocked cell blocks
its entire row and column, find the area of the 
largest continuous unblocked submatrix. 
"""

# --------------------------------------------------- 
# Approach: Sorting + Maximum Gap 
# Time Complexity: O(K log K) 
# Space Complexity: O(K) 
# ---------------------------------------------------

class Solution:
    def largestArea(self, n, m, arr):
        # code here
        blocked_rows = [0, n + 1]
        blocked_cols = [0, m + 1]
        for r, c in arr:
            blocked_rows.append(r)
            blocked_cols.append(c)
        blocked_rows.sort()
        blocked_cols.sort()
        max_rows = 0
        for i in range(1, len(blocked_rows)):
            max_rows = max(max_rows, blocked_rows[i] - blocked_rows[i - 1] - 1)
        max_cols = 0
        for i in range(1, len(blocked_cols)):
            max_cols = max(max_cols, blocked_cols[i] - blocked_cols[i - 1] - 1)
        return max_rows * max_cols
        
