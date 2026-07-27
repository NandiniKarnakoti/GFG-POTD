# Problem: Complete Binary Tree Traversal with Array Input
# Difficulty: Medium
# Date: 27 July 2026

"""
Problem:
Given the level order traversal of a Complete
Binary Tree as an array, return the nodes at
each level after sorting the values within
that level in ascending order.
"""

# ---------------------------------------------------
# Approach: Level-wise Array Traversal
# Time Complexity: O(N log N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def levelSort(self, arr):
        # code here
        ans = []
        i = 0
        level = 1
        n = len(arr)
        while i < n:
            curr = arr[i:min(i + level, n)]
            curr.sort()
            ans.append(curr)
            i += level
            level *= 2
        return ans
        

