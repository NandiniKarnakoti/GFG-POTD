# Problem: High Effort vs Low Effort
# Difficulty: Easy
# Date: 11 August 2026

"""
Problem:
Given two arrays h[] and l[], choose at most one task
per day.

- Low-effort task can be performed on any day.
- High-effort task can be performed on the first day
  or if no task was performed on the previous day.
- A day can also be skipped.

Find the maximum total number of tasks.
"""

# ---------------------------------------------------
# Approach: Dynamic Programming
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def maxTask(self, h: list[int], l: list[int]) -> int:
        # code here
        n = len(h)
        dp = [0] * n
        dp[0] = max(0, l[0], h[0])
        if n == 1:
            return dp[0]
        dp[1] = max(
            dp[0],
            dp[0] + l[1],
            h[1]
        )
        for i in range(2, n):
            dp[i] = max(
                dp[i - 1],         
                dp[i - 1] + l[i],   
                dp[i - 2] + h[i]    
            )
        return dp[n - 1]
        
