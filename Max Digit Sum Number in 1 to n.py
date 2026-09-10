# Problem: Max Digit Sum Number in 1 to n
# Difficulty: Easy
# Date: 9 September 2026

"""
Problem:
Given a number n, find the number in the range from 1 to n
having the maximum digit sum.

If multiple numbers have the same maximum digit sum,
return the largest number.
"""

# ---------------------------------------------------
# Approach: Digit Manipulation
# Time Complexity: O(log N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def findMax(self, n):
        # code here
        ans=n
        p=1
        while n//p>0:
            x=(n//(p*10))*p*10+(n//p%10-1)*p+(p-1)
            if n//p%10>0 and x>=0:
                if sum(map(int,str(x)))>sum(map(int,str(ans))):
                    ans=x
            p*=10
        return ans
