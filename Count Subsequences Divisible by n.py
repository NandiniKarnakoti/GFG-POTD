# Problem: Count Subsequences Divisible by n
# Difficulty: Medium
# Date: 29 August 2026
# Language: Python

"""
Problem:
Given a numeric string s and an integer n, count the number
of non-empty subsequences whose numeric value is divisible by n.

Return the answer modulo 10^9 + 7.
"""

# ---------------------------------------------------
# Approach: Dynamic Programming with Remainders
# Time Complexity: O(|s| * n)
# Space Complexity: O(n)
# ---------------------------------------------------

class Solution:
    def countSubsequences(self, s, n):
        # code here
        MOD = 10**9 + 7
        dp = [0] * n
        for ch in s:
            digit = int(ch)
            new_dp = dp[:]
            for r in range(n):
                new_r = (r * 10 + digit) % n
                new_dp[new_r] = (new_dp[new_r] + dp[r]) % MOD
            new_dp[digit % n] = (new_dp[digit % n] + 1) % MOD
            dp = new_dp
        return dp[0]
        
