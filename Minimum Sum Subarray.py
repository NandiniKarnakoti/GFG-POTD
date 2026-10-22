# Problem: Minimum Sum Subarray
# Difficulty: Medium
# Date: 21 October 2026

"""
Problem:
Find the minimum sum of a non-empty contiguous subarray
in the given array.
"""

# ---------------------------------------------------
# Approach: Modified Kadane's Algorithm
# Time Complexity: O(N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        # code here
        curr=arr[0]
        ans=arr[0]
        for i in range(1,len(arr)):
            curr=min(arr[i],curr+arr[i])
            ans=min(ans,curr)
        return ans
