# Problem: Max Product Subsequence of Size K
# Difficulty: Medium
# Date: 12 September 2026
# Language: Python

"""
Problem:
Given an integer array arr[] and an integer k, find a subsequence
of size k whose product is maximum among all possible subsequences.
Return the maximum product.
"""

# ---------------------------------------------------
# Approach: Dynamic Programming
# Time Complexity: O(N * K)
# Space Complexity: O(N * K)
# ---------------------------------------------------

class Solution:
    def maxProduct(self, arr: list[int], k: int) -> int:
        # code here
        n = len(arr)
        neg_inf = float('-inf')
        pos_inf = float('inf')
        mx = [[neg_inf] * (k + 1) for _ in range(n + 1)]
        mn = [[pos_inf] * (k + 1) for _ in range(n + 1)]
        mx[0][0] = mn[0][0] = 1
        for i in range(1, n + 1):
            x = arr[i - 1]
            mx[i][0] = mn[i][0] = 1
            for j in range(1, min(i, k) + 1):
                a = mx[i - 1][j - 1] * x
                b = mn[i - 1][j - 1] * x
                mx[i][j] = max(mx[i - 1][j], a, b)
                mn[i][j] = min(mn[i - 1][j], a, b)
        return mx[n][k]
