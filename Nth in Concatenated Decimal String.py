# Problem: Nth in Concatenated Decimal String
# Difficulty: Medium
# Date: 28 October 2026

"""
Problem:
Consider a string formed by concatenating the decimal representations
of all positive integers in order: "1234567891011121314...".
Find the nth character using 1-based indexing.
"""

# ---------------------------------------------------
# Approach: Digit-Length Grouping
# Time Complexity: O(log N)
# Space Complexity: O(1)
# ---------------------------------------------------
class Solution:
    def nthCharacter(self, n):
        # code here
        digits=1
        count=9
        start=1
        while n>digits*count:
            n-=digits*count
            digits+=1
            count*=10
            start*=10
        num=start+(n-1)//digits
        return str(num)[(n-1)%digits]
