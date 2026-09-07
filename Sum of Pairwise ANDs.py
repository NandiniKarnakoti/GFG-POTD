# Problem: Sum of Pairwise ANDs
# Difficulty: Medium
# Date: 6 September 2026

"""
Problem:
Given an array arr[], calculate the sum of bitwise AND
for all pairs of elements where i < j.
"""

# ---------------------------------------------------
# Approach: Bit Manipulation
# Time Complexity: O(31 * N) ≈ O(N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def pairAndSum(self, arr):
        # code here
        ans = 0
        for bit in range(31):
            count = 0
            for num in arr:
                if num & (1 << bit):
                    count += 1
            pairs = count * (count - 1) // 2
            ans += pairs * (1 << bit)
        return ans
        
