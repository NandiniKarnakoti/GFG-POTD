# Problem: Closest in BST
# Difficulty: Medium
# Date: 12 November 2026

"""
Problem:
Given the root of a Binary Search Tree (BST) and an integer k,
find the minimum absolute difference between k and the value
of any node in the BST.
"""

# ---------------------------------------------------
# Approach: Iterative DFS + Stack
# Time Complexity: O(N)
# Space Complexity: O(N) in the worst case
# ---------------------------------------------------

'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = self.left = None
        
'''

class Solution:
    def minDiff(self, root: 'Node', k: int) -> int:
        # code here
        ans=float('inf')
        stack=[root]
        while stack:
            node=stack.pop()
            ans=min(ans,abs(node.data-k))
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return ans
        
