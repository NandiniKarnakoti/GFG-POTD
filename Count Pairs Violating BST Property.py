# Problem: Count Pairs Violating BST Property
# Difficulty: Medium
# Date: 23 October 2026

"""
Problem:
Given a binary tree with distinct node values, count the pairs
of nodes that violate the Binary Search Tree (BST) properties.
"""

# ---------------------------------------------------
# Approach: Inorder Traversal + Merge Sort Inversion Count
# Time Complexity: O(N log N)
# Space Complexity: O(N log N)
# ---------------------------------------------------

''' BST Node Structure
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def pairsViolatingBST(self, root):
        # code here
        arr = []
        def inorder(node):
            stack = []
            while stack or node:
                while node:
                    stack.append(node)
                    node = node.left
                node = stack.pop()
                arr.append(node.data)
                node = node.right
        inorder(root)
        def merge_sort(a):
            n = len(a)
            if n <= 1:
                return a, 0
            mid = n // 2
            left, x = merge_sort(a[:mid])
            right, y = merge_sort(a[mid:])
            i = j = count = 0
            merged = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    count += len(left) - i
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged, x + y + count
        return merge_sort(arr)[1]
