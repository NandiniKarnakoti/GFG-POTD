# Problem: Sum of All Digit Subsequences
# Difficulty: Easy
# Date: 15 November 2026

"""
Problem:
Given a string s consisting of digits, find the sum of all
digits across every possible non-empty subsequence.

Return the answer modulo 10^9 + 7.
"""

# ---------------------------------------------------
# Approach: Mathematical Observation + Combinatorics
# Time Complexity: O(N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def subsequenceSum(self, s):
        """code here"""
        MOD=10**9+7
        n=len(s)
        total=sum(int(d) for d in s)
        return (total*pow(2,n-1,MOD))%MOD
