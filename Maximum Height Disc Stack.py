# Problem: Maximum Height Disc Stack
# Difficulty: Hard
# Date: 24 September 2026

"""
Problem:
Given n circular discs with radius r[i] and height h[i],
find the maximum total height of a stack.

A disc can be placed above another disc only when both its
radius and height are strictly smaller than the disc below it.

Each disc can be used at most once.
"""

# ---------------------------------------------------
# Approach: Coordinate Compression + Fenwick Tree DP
# Time Complexity: O(N log N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def maxStackHeight(self, r, h):
        # code here
        n = len(r)
        discs = [(r[i], h[i]) for i in range(n)]
        discs.sort(key=lambda x: (x[0], -x[1]))
        heights = sorted(set(h))
        rank = {x: i + 1 for i, x in enumerate(heights)}
        bit = [0] * (len(heights) + 1)
        def query(i):
            ans = 0
            while i > 0:
                ans = max(ans, bit[i])
                i -= i & -i
            return ans
        def update(i, value):
            while i < len(bit):
                bit[i] = max(bit[i], value)
                i += i & -i
        answer = 0
        for radius, height in discs:
            pos = rank[height]
            current = query(pos - 1) + height
            update(pos, current)
            answer = max(answer, current)
        return answer
