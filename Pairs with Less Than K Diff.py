# Problem: Pairs with Less Than K Diff
# Difficulty: Easy
# Date: 5 August 2026

"""
Problem:
Given an array of positive integers and an integer k,
find the total number of pairs whose absolute
difference is strictly less than k.
"""

# ---------------------------------------------------
# Approach: Sorting + Two Pointers
# Time Complexity: O(N log N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def countPairs(self, arr: list[int], k: int) -> int:
        # code here
        arr.sort()
        n = len(arr)
        i = 0
        ans = 0
        for j in range(n):
            while i < j and arr[j] - arr[i] >= k:
                i += 1
            ans += (j - i)
        return ans
