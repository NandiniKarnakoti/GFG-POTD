# Problem: Minimum Cost for n Characters
# Difficulty: Medium
# Date: 31 August 2026

"""
Problem:
Given n, the cost of inserting one character (i),
deleting the last character (d), and copy-pasting the
entire current string (c), find the minimum cost required
to obtain exactly n characters.

The screen is initially empty.
"""

# ---------------------------------------------------
# Approach: Dynamic Programming + Monotonic Deque
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def minCost(self, n: int, i: int, d: int, c: int) -> int:
        # code here
        from collections import deque
        if n==0:return 0
        dp=[0]*(n+1)
        dp[1]=i
        dq=deque()
        dq.append((1,dp[1]+2*d))
        for j in range(2,n+1):
            left=(j+1)//2
            while dq and dq[0][0]<left:dq.popleft()
            dp[j]=dp[j-1]+i
            if dq:
                dp[j]=min(dp[j],c-j*d+dq[0][1])
            value=dp[j]+2*j*d
            while dq and dq[-1][1]>=value:dq.pop()
            dq.append((j,value))
        return dp[n]
