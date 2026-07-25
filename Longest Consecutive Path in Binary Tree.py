# Problem: Longest Consecutive Path in Binary Tree
# Difficulty: Medium
# Date: 25 July 2026

"""
Problem:
Given the root of a binary tree, find the length
of the longest parent-to-child path where each
child's value is exactly 1 greater than its parent.

Return -1 if no such path exists.
"""

# ---------------------------------------------------
# Approach: DFS Traversal
# Time Complexity: O(N)
# Space Complexity: O(H)
# ---------------------------------------------------

'''
Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def longestConsecutive(self, root):
        # Code here
        self.ans = 1
        def dfs(node, length):
            if not node:
                return
            self.ans = max(self.ans, length)
            if node.left:
                if node.left.data == node.data + 1:
                    dfs(node.left, length + 1)
                else:
                    dfs(node.left, 1)
            if node.right:
                if node.right.data == node.data + 1:
                    dfs(node.right, length + 1)
                else:
                    dfs(node.right, 1)
        if not root:
            return -1
        dfs(root, 1)
        return self.ans if self.ans > 1 else -1
        
