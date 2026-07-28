# Problem: Construct a Full Binary Tree
# Difficulty: Medium
# Date: 28 July 2026

"""
Problem:
Given the preorder traversal of a full binary tree
and the preorder traversal of its mirror tree,
construct the original full binary tree.
"""


''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

# ---------------------------------------------------
# Approach: Recursive Construction + Mirror Index Map
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def constructBinaryTree(self, pre, preMirror):
        # code here
        mp = {}
        for i, x in enumerate(preMirror):
            mp[x] = i
        self.idx = 0
        n = len(pre)
        def build(l, r):
            if self.idx >= n or l > r:
                return None
            root = Node(pre[self.idx])
            self.idx += 1
            if l == r or self.idx == n:
                return root
            pos = mp[pre[self.idx]]
            root.left = build(pos, r)
            root.right = build(l + 1, pos - 1)
            return root
        return build(0, n - 1)
        
