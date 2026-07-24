# Problem: Check Preorder of BST
# Difficulty: Medium
# Date: 24 July 2026

"""
Problem:
Given an array of distinct integers,
determine whether it can represent the
preorder traversal of a Binary Search Tree.
"""

# ---------------------------------------------------
# Approach: Stack + Lower Bound
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def canRepresentBST(self, arr):
        # code here
        stack = []
        root = float("-inf")
        for x in arr:
            if x < root:
                return False
            while stack and x > stack[-1]:
                root = stack.pop()
            stack.append(x)
        return True
        
