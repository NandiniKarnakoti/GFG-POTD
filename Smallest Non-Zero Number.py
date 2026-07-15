# Problem: Smallest Non-Zero Number
# Difficulty: Medium
# Date: 13 July 2026

"""
Problem:
Find the smallest initial value x such that
during the given process, x never becomes
negative.
"""

# ---------------------------------------------------
# Approach: Reverse Greedy
# Time Complexity: O(N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def find(self, arr):
        # code here
        req = 0
        for x in reversed(arr):
            req = (req + x + 1) // 2
        return max(req, 1)

