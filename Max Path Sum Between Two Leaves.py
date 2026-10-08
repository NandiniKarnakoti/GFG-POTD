# Problem: Max Path Sum Between Two Leaves
# Difficulty: Medium
# Date: 7 October 2026

"""
Problem:
Given a binary tree, find the maximum sum of a path that starts at a
leaf node and ends at another leaf node.

The path must pass through at least one non-leaf node. If such a path
does not exist, return -1.
"""

# ---------------------------------------------------
# Approach: DFS + Maximum Root-to-Leaf Sum
# Time Complexity: O(N)
# Space Complexity: O(H)
# ---------------------------------------------------

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:        
    def maxPathSum(self, root):
        # code here
        if root is None:
            return -1
        ans = [-float('inf')]
        def dfs(node):
            if node is None:
                return -float('inf')
            if node.left is None and node.right is None:
                return node.data
            left = dfs(node.left)
            right = dfs(node.right)
            if node.left is not None and node.right is not None:
                ans[0] = max(ans[0], left + node.data + right)
                return node.data + max(left, right)
            if node.left is not None:
                return node.data + left
            return node.data + right
        dfs(root)
        if ans[0] == -float('inf'):
            return -1
        return ans[0]
