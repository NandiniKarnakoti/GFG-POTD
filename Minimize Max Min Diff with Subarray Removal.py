# Problem: Minimize Max Min Diff with Subarray Removal
# Difficulty: Medium
# Date: 26 October 2026

"""
Problem:
Remove a contiguous subarray of size k such that the difference
between the maximum and minimum values in the remaining array
is minimized. Return the minimum possible difference.
"""

# ---------------------------------------------------
# Approach: Prefix and Suffix Min-Max Arrays
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def minDiff(self, k: int, arr: list[int]) -> int:
        # code here
        n=len(arr)
        if k==0:
            return max(arr)-min(arr)
        if k==n:
            return 0
        left_min=[0]*n
        left_max=[0]*n
        right_min=[0]*n
        right_max=[0]*n
        left_min[0]=arr[0]
        left_max[0]=arr[0]
        for i in range(1,n):
            left_min[i]=min(left_min[i-1],arr[i])
            left_max[i]=max(left_max[i-1],arr[i])
        right_min[n-1]=arr[n-1]
        right_max[n-1]=arr[n-1]
        for i in range(n-2,-1,-1):
            right_min[i]=min(right_min[i+1],arr[i])
            right_max[i]=max(right_max[i+1],arr[i])
        ans=float('inf')
        for i in range(n-k+1):
            left=i-1
            right=i+k
            if left<0:
                mn=right_min[right]
                mx=right_max[right]
            elif right>=n:
                mn=left_min[left]
                mx=left_max[left]
            else:
                mn=min(left_min[left],right_min[right])
                mx=max(left_max[left],right_max[right])
            ans=min(ans,mx-mn)
        return ans
