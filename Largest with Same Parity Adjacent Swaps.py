# Problem: Largest with Same Parity Adjacent Swaps
# Difficulty: Medium
# Date: 20 October 2026

"""
Problem:
Given an array arr[], adjacent elements can be swapped only when their
sum is even.

Find the lexicographically largest array obtainable through any number
of allowed swaps.
"""

# ---------------------------------------------------
# Approach: Parity-Based Grouping + Sorting
# Time Complexity: O(N log N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def lexicographicallyLargest(self, arr: list[int]) -> list[int]:
        # code here
        n=len(arr)
        i=0
        while i<n:
            j=i
            while j<n and arr[j]%2==arr[i]%2:
                j+=1
            arr[i:j]=sorted(arr[i:j],reverse=True)
            i=j
        return arr
