# Problem: Shortest Path From 1 To n
# Difficulty: Easy
# Date: 18 October 2026

"""
Problem:
Given a directed graph with vertices numbered from 1 to n, an edge
exists from vertex i to vertex i + 1 or vertex 3 * i, provided the
destination does not exceed n.

Find the minimum number of edges required to reach vertex n from vertex 1.
"""

# ---------------------------------------------------
# Approach: Greedy + Reverse Traversal
# Time Complexity: O(log N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def minimumStep (self, n):
        # code here
        ans=0
        while n>1:
            if n%3==0:
                n//=3
            else:
                n-=1
            ans+=1
        return ans
