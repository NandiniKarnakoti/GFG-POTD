# Problem: Minimum Deletions to Make Sorted
# Difficulty: Easy
# Date: 23 July 2026

"""
Problem:
Given an array, find the minimum number of
elements to delete so that the remaining
elements form a strictly increasing sequence.
"""

# ---------------------------------------------------
# Approach: Longest Increasing Subsequence (Binary Search)
# Time Complexity: O(N log N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def minDeletions(self, arr):
        # code here
        from bisect import bisect_left
        lis = []
        for x in arr:
            i = bisect_left(lis, x)
            if i == len(lis):
                lis.append(x)
            else:
                lis[i] = x
        return len(arr) - len(lis)
        
