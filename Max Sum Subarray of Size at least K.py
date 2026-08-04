# Problem: Max Sum Subarray of Size at least K
# Difficulty: Medium
# Date: 3 August 2026

"""
Problem:
Given an array and an integer k, find the
maximum sum among all contiguous subarrays
having a length greater than or equal to k.
"""

# ---------------------------------------------------
# Approach: Kadane's Algorithm + Sliding Window
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def maxSumWithK(self, arr: list[int], k: int) -> int:
        # code here
        n = len(arr)
        max_end = [0] * n
        max_end[0] = arr[0]
        for i in range(1, n):
            max_end[i] = max(arr[i], max_end[i - 1] + arr[i])
        window_sum = sum(arr[:k])
        ans = window_sum
        for i in range(k, n):
            window_sum += arr[i] - arr[i - k]
            ans = max(ans, window_sum)
            ans = max(ans, window_sum + max_end[i - k])
        return ans
        
