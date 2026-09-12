# Problem: Values with Equal Array Remainders
# Difficulty: Easy
# Date: 11 September 2026

"""
Problem:
Given an integer array arr[], count the number of positive integers k
such that all elements of the array leave the same remainder when
divided by k.

If infinitely many values of k satisfy the condition, return -1.
"""

# ---------------------------------------------------
# Approach: GCD of Differences + Divisor Enumeration
# Time Complexity: O(N + sqrt(G))
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def sameMod(self, arr):
        # code here
        from math import gcd
        g=0
        for x in arr[1:]:
            g=gcd(g,abs(x-arr[0]))
        if g==0:
            return -1
        ans=0
        i=1
        while i*i<=g:
            if g%i==0:
                ans+=1
                if i!=g//i:
                    ans+=1
            i+=1
        return ans
