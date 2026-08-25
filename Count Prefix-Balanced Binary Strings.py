# Problem: Count Prefix-Balanced Binary Strings
# Difficulty: Medium
# Date: 25 August 2026
# Language: Python

"""
Problem:
Given an integer n, count the number of binary strings of length
2 * n containing exactly n ones and n zeros such that every prefix
contains at least as many ones as zeros.

Return the answer modulo 10^9 + 7.
"""

# ---------------------------------------------------
# Approach: Catalan Number + Modular Inverse
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def prefixStrings(self, n: int) -> int:
        # code here
        MOD = 10**9 + 7
        fact = [1] * (2 * n + 1)
        for i in range(1, 2 * n + 1):
            fact[i] = (fact[i - 1] * i) % MOD
        numerator = fact[2 * n]
        denominator = (fact[n] * fact[n + 1]) % MOD
        return (numerator * pow(denominator, MOD - 2, MOD)) % MOD
