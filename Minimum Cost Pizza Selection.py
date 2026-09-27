# Problem: Minimum Cost Pizza Selection
# Difficulty: Medium
# Date: 26 September 2026

"""
Problem:
Given the areas and costs of Small, Medium, and Large pizzas,
find the minimum cost required to buy pizzas whose total area
is at least x.

Any number of pizzas of each type can be purchased.
"""

# ---------------------------------------------------
# Approach: Brute Force + Greedy for Remaining Area
# Time Complexity: O((X/S) * (X/M))
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def minimumCost(self, x, s, m, l, cs, cm, cl):
        # code here
        ans = float('inf')
        for i in range(x // s + 2):
            for j in range(x // m + 2):
                area = i * s + j * m
                if area >= x:
                    ans = min(ans, i * cs + j * cm)
                    continue
                remaining = x - area
                k = (remaining + l - 1) // l
                cost = i * cs + j * cm + k * cl
                ans = min(ans, cost)
        return ans
