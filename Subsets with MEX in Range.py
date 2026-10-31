# Problem: Subsets with MEX in Range
# Difficulty: Hard
# Date: 30 October 2026

"""
Problem:
Given an array arr and a range [l, r], count the number of subsets
whose MEX (Minimum Excluded non-negative integer) lies in [l, r].
Return the answer modulo 10^9 + 7.
"""

# ---------------------------------------------------
# Approach: Frequency Counting + Prefix Product
# Time Complexity: O(N + R log MOD)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def cntSubsets(self, arr: List[int], l: int, r: int) -> int:
        """ code here """
        MOD=10**9+7
        n=len(arr)
        freq=[0]*(n+1)
        for x in arr:
            if x<=n:
                freq[x]+=1
        ans=0
        product=1
        prefix_count=0
        for k in range(r+1):
            if k>0:
                product=product*(pow(2,freq[k-1],MOD)-1)%MOD
            prefix_count+=freq[k]
            greater_count=n-prefix_count
            count=product*pow(2,greater_count,MOD)%MOD
            if l<=k<=r:
                ans=(ans+count)%MOD
            if freq[k]==0:
                product=0
        return ans
