# GeeksForGeeks POTD
# Problem: Number of Turns in Binary Tree
# Difficulty: Hard
# Date: 22 August 2026

"""
Problem:
Given two nodes p and q in a binary tree, count the
number of turns required while travelling from node p
to node q.

A turn occurs whenever the direction changes from
Left to Right or Right to Left.

If there are no turns, return -1.
"""

# ---------------------------------------------------
# Approach: Root Paths + Direction Comparison
# Time Complexity: O(N)
# Space Complexity: O(H)
# ---------------------------------------------------

''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def numberOfTurns(self, root, p, q):
        # code here
        def path(node,target,arr):
            if not node:
                return False
            if node.data==target:
                return True
            arr.append('L')
            if path(node.left,target,arr):
                return True
            arr.pop()
            arr.append('R')
            if path(node.right,target,arr):
                return True
            arr.pop()
            return False
        p_path=[]
        q_path=[]
        path(root,p,p_path)
        path(root,q,q_path)
        i=0
        while i<len(p_path) and i<len(q_path) and p_path[i]==q_path[i]:
            i+=1
        directions=p_path[i:][::-1]+q_path[i:]
        turns=0
        for i in range(1,len(directions)):
            if directions[i]!=directions[i-1]:
                turns+=1
        return turns if turns else -1
        
        
