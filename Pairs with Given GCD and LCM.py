# Problem: Pairs with Given GCD and LCM
# Difficulty: Easy
# Date: 10 September 2026

"""
Problem:
Given the GCD (x) and LCM (y) of two positive integers,
count the number of valid ordered pairs (a, b).

Pairs (a, b) and (b, a) are counted as distinct when a != b.
"""

# ---------------------------------------------------
# Approach: Divisor Enumeration + GCD
# Time Complexity: O(sqrt(y / x))
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def pairCount(self, x, y):
        """code here"""
        if y % x != 0:
            return 0
        n = y // x
        count = 0
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                j = n // i
                if __import__('math').gcd(i, j) == 1:
                    if i == j:
                        count += 1
                    else:
                        count += 2
        return count
