# Problem: Pyramid Array with Reduce Operations
# Difficulty: Medium
# Date: 23 September 2026

"""
Problem:
Given an array arr[] representing the heights of stones, transform
the array into a valid pyramid by only reducing stone heights.

A valid pyramid has the form:
1, 2, 3, ..., x, ..., 3, 2, 1

All stones outside the chosen pyramid must have height 0.

Find the minimum total cost of reductions.
"""

# ---------------------------------------------------
# Approach: Dynamic Programming on Both Sides
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def formPyramid(self, arr):
        # code here 
        n=len(arr)
        left=[0]*n
        right=[0]*n
        left[0]=min(arr[0],1)
        for i in range(1,n):
            left[i]=min(arr[i],left[i-1]+1)
        right[n-1]=min(arr[n-1],1)
        for i in range(n-2,-1,-1):
            right[i]=min(arr[i],right[i+1]+1)
        max_saved=0
        for i in range(n):
            peak=min(left[i],right[i])
            max_saved=max(max_saved,peak*peak)
        return sum(arr)-max_saved
