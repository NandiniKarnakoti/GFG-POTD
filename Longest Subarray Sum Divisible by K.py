# Problem: Longest Subarray Sum Divisible by K
# Difficulty: Medium
# Date: 22 November 2026
# Language: Python

"""
Problem:
Find the length of the longest subarray whose sum
is divisible by k.

Return 0 if no such subarray exists.
"""

# ---------------------------------------------------
# Approach: Prefix Sum + Hash Map
# Time Complexity: O(N)
# Space Complexity: O(K)
# ---------------------------------------------------

class Solution:
	def longestSubarrayDivK(self, arr, k):
		# code here
        d={0:-1}
        s=0
        ans=0
        for i in range(len(arr)):
            s+=arr[i]
            rem=s%k
            if rem in d:
                ans=max(ans,i-d[rem])
            else:
                d[rem]=i
        return ans
