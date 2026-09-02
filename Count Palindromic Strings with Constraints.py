# Problem: Count Palindromic Strings with Constraints
# Difficulty: Medium
# Date: 2 September 2026
# Language: Python

"""
Problem:
Given integers n and k, count the number of palindromic strings
of length less than or equal to n using the first k lowercase letters.

No character can appear more than twice.

Return the answer modulo 10^9 + 7.
"""

# ---------------------------------------------------
# Approach: Combinatorics
# Time Complexity: O(N * K)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def palindromicStrings(self, n, k):
        # code here
        MOD = 10**9 + 7
        ans = 0
        for length in range(1, n + 1):
            half = length // 2
            ways = 1
            for i in range(half):
                ways = (ways * (k - i)) % MOD
            if length % 2 == 1:
                ways = (ways * (k - half)) % MOD
            ans = (ans + ways) % MOD
        return ans
        
