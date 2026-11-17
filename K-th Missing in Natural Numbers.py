# Problem: K-th Missing in Natural Numbers
# Difficulty: Medium
# Date: 16 November 2026

"""
Problem:
Given an array of distinct positive integers and a positive
integer k, find the k-th smallest positive integer missing
from the array.
"""

# ---------------------------------------------------
# Approach: Sorting + Greedy
# Time Complexity: O(N log N)
# Space Complexity: O(1) auxiliary space
# ---------------------------------------------------

class Solution:
    def findKthSmall(self, arr, k):
        # code here
        arr.sort()
        ans=k
        for i in arr:
            if i<=ans:
                ans+=1
            else:
                break
        return ans
        
