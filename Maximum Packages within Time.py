# Problem: Maximum Packages within Time
# Difficulty: Easy
# Date: 31 October 2026

"""
Problem:
Given an array where arr[i] represents the number of packages
at location i, find the maximum number of packages that can
be delivered by visiting consecutive locations within totalTime.
Each location takes 1 unit of time.
"""

# ---------------------------------------------------
# Approach: Sliding Window
# Time Complexity: O(N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def maxPackages(self, arr: list[int], totalTime: int) -> int:
        # code here
        window=sum(arr[:totalTime])
        maximum=window
        for i in range(totalTime,len(arr)):
            window+=arr[i]-arr[i-totalTime]
            maximum=max(maximum,window)
        return maximum
