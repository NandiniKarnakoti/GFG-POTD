# Problem: Friends Pairing Problem
# Difficulty: Medium
# Date: 8 August 2026

"""
Problem:
Given n friends, each friend can either remain
single or pair up with exactly one other friend.

Find the total number of possible arrangements.
"""

# ---------------------------------------------------
# Approach: Dynamic Programming with Constant Space
# Time Complexity: O(N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def countFriendsPairings(self, n: int) -> int:
        # code here 
        MOD = 10**9 + 7
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return 2
        a = 1
        b = 2
        for i in range(3, n + 1):
            c = (b + (i - 1) * a) % MOD
            a = b
            b = c
        return b
