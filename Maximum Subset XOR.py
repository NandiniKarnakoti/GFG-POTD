# Problem: Maximum Subset XOR
# Difficulty: Medium
# Date: 30 July 2026

"""
Problem:
Given an array, choose any subset of elements
such that the XOR of the chosen elements is
maximized.
"""

# ---------------------------------------------------
# Approach: XOR Basis (Gaussian Elimination)
# Time Complexity: O(32 × N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def maxSubsetXOR(self, arr):
        # code here
        n=len(arr)
        idx=0
        for bit in range(31,-1,-1):
            mx=idx
            while mx<n and ((arr[mx]>>bit)&1)==0:
                mx+=1
            if mx==n:
                continue
            arr[idx],arr[mx]=arr[mx],arr[idx]
            for j in range(n):
                if j!=idx and ((arr[j]>>bit)&1):
                    arr[j]^=arr[idx]
            idx+=1
        ans=0
        for x in arr:
            ans=max(ans,ans^x)
        return ans
