# Problem: Max After m Range Increments
# Difficulty: Medium
# Date: 2 August 2026

"""
Problem:
Given m range increment operations on an initially
zero-filled array of size n, find the maximum
value in the array after performing all operations.
"""

# ---------------------------------------------------
# Approach: Difference Array + Prefix Sum
# Time Complexity: O(N + M)
# Space Complexity: O(N)
# ---------------------------------------------------


class Solution:
    def findMax(self, n, a, b, k):
        # code here
        diff = [0] * (n + 1)
        for i in range(len(a)):
            diff[a[i]] += k[i]
            if b[i] + 1 < n:
                diff[b[i] + 1] -= k[i]
        curr = 0
        ans = 0
        for i in range(n):
            curr += diff[i]
            ans = max(ans, curr)
        return ans
        
