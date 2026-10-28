# Problem: Maximum Weight Transformation of String
# Difficulty: Medium
# Date: 27 October 2026

"""
Problem:
Given a string containing only 'A' and 'B', maximize its weight
by choosing non-overlapping alternating adjacent pairs.
Each pair contributes 4, each unpaired character contributes 1,
and every toggle decreases the total weight by 1.
"""

# ---------------------------------------------------
# Approach: Dynamic Programming
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def getMaxWeight(self, s):
        # code here
        n=len(s)
        dp=[0]*(n+1)
        for i in range(1,n+1):
            dp[i]=dp[i-1]+1
            if i>=2:
                cost=0 if s[i-2]!=s[i-1] else 1
                dp[i]=max(dp[i],dp[i-2]+4-cost)
        return dp[n]
