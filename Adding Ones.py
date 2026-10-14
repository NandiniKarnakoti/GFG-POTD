# Problem: Adding Ones
# Difficulty: Easy
# Date: 13 October 2026

"""
Problem:
Given an array of size n initially filled with zeros and an array of
updates containing 1-based indices, increment every element whose index
is greater than or equal to each update value.

Apply all updates and return the modified array.
"""

# ---------------------------------------------------
# Approach: Frequency Counting + Prefix Sum
# Time Complexity: O(N + K)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def update(self, n: int, updates: list[int]) -> list[int]:
        # code here
        arr=[0]*n
        for j in updates:
            arr[j-1]+=1
        for i in range(1,n):
            arr[i]+=arr[i-1]
        return arr
            
