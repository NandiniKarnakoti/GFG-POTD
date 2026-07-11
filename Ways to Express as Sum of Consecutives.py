# Problem: Ways to Express as Sum of Consecutives
# Difficulty: Medium
# Date: 9 July 2026

"""
Problem:
Count the number of ways to express n
as a sum of two or more consecutive
natural numbers.
"""
# ---------------------------------------------------
# Approach: Mathematical Observation
# Time Complexity: O(√N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def getCount(self, n):
        # code here 
        count = 0
        k = 2
        while k * (k + 1) // 2 <= n:
            rem = n - k * (k - 1) // 2
            if rem > 0 and rem % k == 0:
                count += 1
            k += 1
        return count
