# Problem: Balancing with Distinct Powers
# Difficulty: Easy
# Date: 10 October 2026

"""
Problem:
Given a target weight b and a base a, determine whether a weighing scale
can be balanced using distinct powers of a.

Check whether:
b + (some powers of a) = (some other powers of a)

Each power of a can be used at most once.
"""

# ---------------------------------------------------
# Approach: Base-a Representation + Greedy
# Time Complexity: O(log_a B)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def balancePan(self, a, b):
        # code here
        while b>0:
            remainder=b % a
            if remainder==1:
                b-=1
            elif remainder==a-1:
                b+=1
            elif remainder!=0:
                return False
            b//=a
        return True
        
