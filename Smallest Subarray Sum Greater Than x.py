# Problem: Smallest Subarray Sum Greater Than x
# Difficulty: Easy
# Date: 21 November 2026
# Language: Python

"""
Problem:
Find the length of the smallest subarray whose sum
is strictly greater than x.

Return 0 if no such subarray exists.
"""

# ---------------------------------------------------
# Approach: Sliding Window (Two Pointers)
# Time Complexity: O(N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def smallestSubWithSum(self, arr, x):
        # code here 
        start=0
        curr=0
        min_val=float('inf')
        for i in range(len(arr)):
            curr+=arr[i]
            while curr>x:
                min_val=min(min_val,i-start+1)
                curr-=arr[start]
                start+=1
        return 0 if min_val==float('inf') else min_val
                
        
        
