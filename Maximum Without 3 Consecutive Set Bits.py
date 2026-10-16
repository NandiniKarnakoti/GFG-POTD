# Problem: Maximum Without 3 Consecutive Set Bits
# Difficulty: Medium
# Date: 16 October 2026
# Language: Python

"""
Problem:
Given a non-negative integer n, find the maximum possible value after
changing zero or more set bits (1) to unset bits (0), such that its
binary representation does not contain three consecutive set bits.
"""

# ---------------------------------------------------
# Approach: Bit Manipulation + Greedy
# Time Complexity: O(log N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def maxValue(self, n: int) -> int:
        """code here"""
        while n & (n >> 1) & (n >> 2):
            bit = (n & (n >> 1) & (n >> 2)).bit_length() - 1
            n &= ~(1 << bit)
        return n
