# Problem: Minimum Elements Outside Subsequences
# Difficulty: Hard
# Date: 7 September 2026

"""
Problem:
Given an array arr[], partition its elements into:

- One strictly increasing subsequence
- One strictly decreasing subsequence

Each element can belong to at most one subsequence.

Return the minimum number of elements that cannot be included
in either subsequence.
"""

# ---------------------------------------------------
# Approach: Dynamic Programming with States
# Time Complexity: O(N * M²)
# Space Complexity: O(M²)
# ---------------------------------------------------

class Solution:
    def minCount(self, arr):
        """ code here """
        n = len(arr)
        dp = {(0, 101): 0}
        for x in arr:
            new_dp = dp.copy()
            for (inc, dec), count in dp.items():
                if x > inc:
                    state = (x, dec)
                    new_dp[state] = max(
                        new_dp.get(state, 0),
                        count + 1
                    )
                if x < dec:
                    state = (inc, x)
                    new_dp[state] = max(
                        new_dp.get(state, 0),
                        count + 1
                    )
            dp = new_dp
        max_selected = max(dp.values())
        return n - max_selected
