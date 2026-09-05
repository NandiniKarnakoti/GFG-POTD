# Problem: Bird and Max Fruit Gathering
# Difficulty: Easy
# Date: 4 September 2026

"""
Problem:
Given fruit values of trees arranged in a circle and an integer m,
find the maximum total fruits a bird can collect by visiting at most
m neighboring trees.

The first and last trees are considered neighbors.
"""

# ---------------------------------------------------
# Approach: Circular Sliding Window
# Time Complexity: O(N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def maxFruits(self, arr: list[int], m: int) -> int:
        """ code here """
        n = len(arr)
        if m >= n:
            return sum(arr)
        current_sum = sum(arr[:m])
        max_sum = current_sum
        for i in range(1, n):
            current_sum -= arr[i - 1]
            current_sum += arr[(i + m - 1) % n]
            max_sum = max(max_sum, current_sum)
        return max_sum
