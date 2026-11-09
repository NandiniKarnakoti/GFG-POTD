# Problem: Minimum Time with 2 Scanners
# Difficulty: Easy
# Date: 9 November 2026

"""
Problem:
Given n documents and two scanners with scanning times
s1 and s2 per document, find the minimum time required
to scan all documents.

Both scanners can work simultaneously.
"""

# ---------------------------------------------------
# Approach: Brute Force + Minimum Time Calculation
# Time Complexity: O(N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def minTime(self, n: int, s1: int, s2: int) -> int:
        # code here
        ans=float('inf')
        for i in range(n+1):
            t=max(i*s1,(n-i)*s2)
            ans=min(ans,t)
        return ans
