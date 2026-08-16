# Problem: Numbers Without d as Digit
# Difficulty: Hard
# Date: 15 August 2026

"""
Problem:
Given n and a digit d, count the numbers from 1 to n
that do not contain digit d in their decimal representation.
"""

# ---------------------------------------------------
# Approach: Digit Counting
# Time Complexity: O(log N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def countWithout(self, n: int, d: int) -> int:
        # code here
        digits=list(map(int,str(n)))
        dp=[[0,0],[0,0]]
        dp[1][0]=1
        for digit in digits:
            new_dp=[[0,0],[0,0]]
            for tight in range(2):
                for started in range(2):
                    ways=dp[tight][started]
                    if ways==0:
                        continue
                    limit=digit if tight else 9
                    for x in range(limit+1):
                        if x==d and (started or d!=0):
                            continue
                        new_tight=1 if tight and x==digit else 0
                        new_started=1 if started or x!=0 else 0
                        new_dp[new_tight][new_started]+=ways
            dp=new_dp
        return dp[0][1]+dp[1][1]
