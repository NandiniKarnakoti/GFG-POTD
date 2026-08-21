# Problem: Node and Ancestor Max Diff
# Difficulty: Medium
# Date: 20 August 2026
# Language: Python

"""
Problem:
Given the root of a binary tree, find the maximum
difference between an ancestor node A and its
descendant node B.

We need to maximize:
A - B
"""

# ---------------------------------------------------
# Approach: DFS + Minimum Descendant Value
# Time Complexity: O(N)
# Space Complexity: O(H)
# ---------------------------------------------------

''' Structure of Binary Tree Node
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def maxDiff(self, root):
        # code here
        self.max_difference = float('-inf')
        def dfs(node):
            if not node:
                return float('inf')
            if not node.left and not node.right:
                return node.data
            left_min = dfs(node.left)
            right_min = dfs(node.right)
            min_descendant = min(left_min, right_min)
            self.max_difference = max(
                self.max_difference,
                node.data - min_descendant
            )
            return min(node.data, min_descendant)
        dfs(root)
        return self.max_difference
        
