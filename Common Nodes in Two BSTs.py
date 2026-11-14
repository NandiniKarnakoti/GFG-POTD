# Problem: Common Nodes in Two BSTs
# Difficulty: Medium
# Date: 13 November 2026

"""
Problem:
Given the roots of two Binary Search Trees, find all node
values present in both trees.

Return the common values in sorted order.
"""

# ---------------------------------------------------
# Approach: Inorder Traversal + Two Pointers
# Time Complexity: O(N + M)
# Space Complexity: O(N + M)
# ---------------------------------------------------

''' 
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findCommon(self, r1: 'Node', r2: 'Node') -> list[int]:
        # code here
        def inorder(root):
            res=[]
            stack=[]
            curr=root
            while curr or stack:
                while curr:
                    stack.append(curr)
                    curr=curr.left
                curr=stack.pop()
                res.append(curr.data)
                curr=curr.right
            return res
        a=inorder(r1)
        b=inorder(r2)
        i=j=0
        ans=[]
        while i<len(a) and j<len(b):
            if a[i]==b[j]:
                ans.append(a[i])
                i+=1
                j+=1
            elif a[i]<b[j]:
                i+=1
            else:
                j+=1
        return ans
