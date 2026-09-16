# Problem: Visit Leaves with Budget
# Difficulty: Easy
# Date: 15 September 2026

"""
Problem:
Given a binary tree and a budget k, the cost of visiting a leaf
node is equal to its level, with the root at level 1.

Return the maximum number of leaf nodes that can be visited
without exceeding the given budget.
"""

# ---------------------------------------------------
# Approach: BFS + Sorting + Greedy
# Time Complexity: O(N log N)
# Space Complexity: O(N)
# ---------------------------------------------------

''' Binary Tree Node Structure
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getCount(self, root, k):
        # code here
        from collections import deque
        if not root:
            return 0
        q = deque([(root, 1)])
        costs = []
        while q:
            node, level = q.popleft()
            if not node.left and not node.right:
                costs.append(level)
            else:
                if node.left:
                    q.append((node.left, level + 1))
                if node.right:
                    q.append((node.right, level + 1))
        costs.sort()
        count = 0
        for cost in costs:
            if k < cost:
                break
            k -= cost
            count += 1
        return count
        
