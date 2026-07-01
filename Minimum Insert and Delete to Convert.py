# Problem: Minimum Insert and Delete to Convert 
# Difficulty: Hard
# Date: 30 June 2026

""" 
Problem:
Find the minimum insertions and deletions
required to convert array a into array b.

Array b is sorted and contains distinct elements. 
"""
# --------------------------------------------------- 
# Approach: Mapping + Longest Increasing Subsequence 
# Time Complexity: O((N + M) log M) 
# Space Complexity: O(M) 
# ---------------------------------------------------

class Solution:
    def minInsAndDel(self, a, b):
        # code here
        from bisect import bisect_left
        pos = {val: i for i, val in enumerate(b)}
        arr = []
        for x in a:
            if x in pos:
                arr.append(pos[x])
        lis = []
        for x in arr:
            idx = bisect_left(lis, x)
            
            if idx == len(lis):
                lis.append(x)
            else:
                lis[idx] = x
        L = len(lis)
        return len(a) + len(b) - 2 * L
