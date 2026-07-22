# Problem: Maximum Reachable Index Difference
# Difficulty: Medium
# Date: 21 July 2026

"""
Problem:
Given a string of lowercase letters, start from any
index containing 'a' and repeatedly jump to the right
to an occurrence of the next alphabet character.

Find the maximum possible difference between the
starting and ending indices.
Return -1 if there is no 'a' in the string.
"""

# ---------------------------------------------------
# Approach: Reverse DP + Best Reachable Index
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def maxIndexDifference(self, s):
        # code here
        n = len(s)
        reach = [0] * n
        best = [-1] * 26
        ans = -1
        for i in range(n - 1, -1, -1):
            c = ord(s[i]) - ord('a')
            if c == 25:
                reach[i] = i
            elif best[c + 1] != -1:
                reach[i] = best[c + 1]
            else:
                reach[i] = i
            best[c] = max(best[c], reach[i])
            if c == 0:
                ans = max(ans, reach[i] - i)
        return ans
        
