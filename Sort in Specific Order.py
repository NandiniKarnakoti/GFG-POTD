# Problem: Sort in Specific Order
# Difficulty: Medium
# Date: 19 November 2026

"""
Problem:
Given an array of non-negative integers, rearrange it so that:
1. Odd numbers appear first in descending order.
2. Even numbers appear next in ascending order.
"""

# ---------------------------------------------------
# Approach: Partitioning + Sorting
# Time Complexity: O(N log N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def sortIt(self, arr):
        # code here
        odd=[]
        even=[]
        for i in arr:
            if i%2!=0:
                odd.append(i)
            else:
                even.append(i)
        odd.sort(reverse=True)
        even.sort()
        arr[:]=odd+even
        
        
    
