# Problem: Minimum Absolute Difference In BST
# Difficulty: Medium
# Date: 19 September 2026
# Language: Python

"""
Problem:
Given the root of a Binary Search Tree (BST), find the minimum
absolute difference between the values of any two different nodes.
"""

# ---------------------------------------------------
# Approach: Iterative Inorder Traversal
# Time Complexity: O(N)
# Space Complexity: O(H)
# ---------------------------------------------------

'''
Binary Tree Node Structure
class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
'''
        
class Solution:
    def absDiff(self, root):
        # code here
        stack = []
        curr = root
        prev = None
        ans = float('inf')
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev is not None:
                ans = min(ans, curr.data - prev)
            prev = curr.data
            curr = curr.right
        return ans
