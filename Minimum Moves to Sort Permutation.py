# Problem: Minimum Moves to Sort Permutation
# Difficulty: Medium
# Date: 26 August 2026

"""
Problem:
Given a permutation containing integers from 1 to n exactly once,
sort the array in ascending order.

In one operation, any element can be moved either to the beginning
or to the end of the array.

Return the minimum number of operations required.
"""

# ---------------------------------------------------
# Approach: Position Array
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def minMoves(self, arr):
        """code here"""
        n = len(arr)
        pos = [0] * (n + 1)
        for i in range(n):
            pos[arr[i]] = i
        longest = 1
        current = 1
        for x in range(1, n):
            if pos[x] < pos[x + 1]:
                current += 1
            else:
                current = 1
            longest = max(longest, current)
        return n - longest
