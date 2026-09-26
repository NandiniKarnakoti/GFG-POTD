# Problem: Box Stacking
# Difficulty: Hard
# Date: 25 September 2026

"""
Problem:
Given three arrays representing the height, width, and length
of different boxes, find the maximum possible height of a stack.

Each box can be rotated so that any dimension becomes its height.
A box can be placed on another only if both dimensions of its base
are strictly smaller than the base dimensions of the box below.

Multiple instances of the same box type can be used.
"""

# ---------------------------------------------------
# Approach: Rotation Generation + Dynamic Programming
# Time Complexity: O(N^2)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def maxHeight(self, height: list[int], width: list[int], length: list[int]) -> int:
        # Code here
        boxes = []
        for h, w, l in zip(height, width, length):
            boxes.append((max(w, l), min(w, l), h))
            boxes.append((max(h, l), min(h, l), w))
            boxes.append((max(h, w), min(h, w), l))
        boxes.sort(reverse=True)
        n = len(boxes)
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            base_l, base_w, h = boxes[i]
            dp[i] = h
            for j in range(i + 1, n):
                top_l, top_w, top_h = boxes[j]
                if top_l < base_l and top_w < base_w:
                    dp[i] = max(dp[i], h + dp[j])
        return max(dp)
