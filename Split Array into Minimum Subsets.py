# Problem: Split Array into Minimum Subsets
# Difficulty: Easy
# Date: 30 July 2026

"""
Problem:
Given an array of distinct positive integers,
split it into the minimum number of subsets
such that each subset contains consecutive numbers.
"""

# ---------------------------------------------------
# Approach: Sort and Count Consecutive Groups
# Time Complexity: O(N log N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def minSubsets(self, arr):
        #code here
        if not arr:
            return 0
        arr.sort()
        ans = 1
        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1] + 1:
                ans += 1
        return ans
