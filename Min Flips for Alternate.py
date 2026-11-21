# Problem: Min Flips for Alternate
# Difficulty: Medium
# Date: 20 November 2026
# Language: Python

"""
Problem:
Given a binary string s, find the minimum number of
flips required to make it alternating.

An alternating string has no two adjacent characters equal.
"""

# ---------------------------------------------------
# Approach: Greedy + Pattern Comparison
# Time Complexity: O(N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def minFlips(self, s):
        # Code here
        z_c=0
        for i in range(len(s)):
            expected='0' if i%2==0 else '1'
            if expected!=s[i]:
                z_c+=1
        o_c=len(s)-z_c
        return min(z_c,o_c)
        
