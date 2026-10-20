# Problem: Count Indices That Escape Array
# Difficulty: Medium
# Date: 19 October 2026

"""
Problem:
Given an array arr[], where arr[i] represents the number of steps to
move from index i, determine how many indices eventually lead outside
the array.

Positive values move right, negative values move left, and zero values
are considered bad. Indices that enter an infinite cycle are also bad.
"""

# ---------------------------------------------------
# Approach: Graph Traversal + State Marking
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def goodIndices(self, arr):
        # code here
        n=len(arr)
        state=[0]*n
        ans=0
        for i in range(n):
            if state[i]!=0:
                continue
            path=[]
            j=i
            while 0<=j<n and state[j]==0:
                state[j]=1
                path.append(j)
                if arr[j]==0:
                    break
                j+=arr[j]
            if j<0 or j>=n:
                res=2
            elif state[j]==2:
                res=2
            else:
                res=3
            for k in reversed(path):
                state[k]=res
        return state.count(2)
