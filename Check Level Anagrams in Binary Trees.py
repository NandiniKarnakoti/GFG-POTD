# Problem: Check Level Anagrams in Binary Trees
# Difficulty: Medium
# Date: 21 September 2026

"""
Problem:
Given the roots of two binary trees, check whether the nodes at
every corresponding level of the two trees are anagrams.

Two levels are anagrams if they contain the same node values with
the same frequencies, regardless of their order.
"""

# ---------------------------------------------------
# Approach: Level Order Traversal + Frequency Comparison
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

"""
Structure of binary tree Node
class Node:
    def __init__(self, x: int):
        self.data = x
        self.left = self.right = None
"""
class Solution:
    def areAnagrams(self, root1, root2):
        """ code here """
        from collections import deque, Counter
        q1 = deque([root1])
        q2 = deque([root2])
        while q1 and q2:
            n1 = len(q1)
            n2 = len(q2)
            if n1 != n2:
                return False
            level1 = []
            level2 = []
            for _ in range(n1):
                node = q1.popleft()
                level1.append(node.data)
                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)
            for _ in range(n2):
                node = q2.popleft()
                level2.append(node.data)
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            if Counter(level1) != Counter(level2):
                return False
        return not q1 and not q2
