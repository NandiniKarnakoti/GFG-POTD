# Problem: Roll Characters of String
# Difficulty: Medium
# Date: 14 October 2026

"""
Problem:
Given a string s consisting of lowercase English letters and an array
roll[], increment each of the first roll[i] characters by one position
in the English alphabet for every roll operation.

After 'z', the character wraps around to 'a'.

Return the final string after applying all operations.
"""

# ---------------------------------------------------
# Approach: Difference Array + Prefix Sum
# Time Complexity: O(N + K)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def findRollOut(self, s, roll):
        # code here
        n = len(s)
        diff = [0] * (n + 1)
        for r in roll:
            diff[0] += 1
            diff[r] -= 1
        res = []
        total = 0
        for i in range(n):
            total += diff[i]
            res.append(chr((ord(s[i]) - ord('a') + total) % 26 + ord('a')))
        return ''.join(res)
