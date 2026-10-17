# Problem: Successful Binary Searches Irrespective of Pivot
# Difficulty: Medium
# Date: 17 October 2026

"""
Problem:
Given an array of distinct integers, count the elements for which a
binary search is guaranteed to succeed regardless of the pivot choices.
"""

# ---------------------------------------------------
# Approach: Prefix Maximum + Suffix Minimum
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def countAlwaysFound(self, arr):
        # code here
        n=len(arr)
        prefix_max=[0]*n
        suffix_min=[0]*n
        prefix_max[0]=arr[0]
        for i in range(1,n):
            prefix_max[i]=max(prefix_max[i-1],arr[i])
        suffix_min[n-1]=arr[n-1]
        for i in range(n-2,-1,-1):
            suffix_min[i]=min(suffix_min[i+1],arr[i])
        count=0
        for i in range(n):
            if arr[i]==prefix_max[i] and arr[i]==suffix_min[i]:
                count+=1
        return count
        
