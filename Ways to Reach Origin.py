# Problem: Ways to Reach Origin
# Difficulty: Medium
# Date: 30 September 2026

"""
Problem:
Given a point (x, y), find the number of distinct paths to reach
the origin (0, 0).

From any point, Geek can move:
- Left:  (x, y) -> (x - 1, y)
- Down:  (x, y) -> (x, y - 1)

Return the answer modulo 10^9 + 7.
"""

# ---------------------------------------------------
# Approach: Dynamic Programming with Space Optimization
# Time Complexity: O(X * Y)
# Space Complexity: O(Y)
# ---------------------------------------------------

class Solution:
    def ways(self, x: int, y: int) -> int:
        # code here
        MOD=10**9+7
        dp=[0]*(y+1)
        dp[0]=1
        for i in range(x+1):
            for j in range(1,y+1):
                dp[j]=(dp[j]+dp[j-1])%MOD
        return dp[y]
        
