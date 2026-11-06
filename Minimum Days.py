# Problem: Minimum Days
# Difficulty: Medium
# Date: 5 November 2026

"""
Problem:
Given a string s and a permutation p[], replace characters
with '?' in the specified order.

Find the minimum number of days required so that no two
adjacent non-'?' characters are equal.
"""

# ---------------------------------------------------
# Approach: Incremental Updates + Adjacent Pair Counting
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def getMinimumDays(self, s: str, p: list[int]) -> int:
        # code here
        n=len(s)
        a=list(s)
        bad=0
        for i in range(n-1):
            if a[i]==a[i+1]:
                bad+=1
        if bad==0:
            return 0
        for i in range(n):
            x=p[i]
            if x>0 and a[x]==a[x-1]:
                bad-=1
            if x<n-1 and a[x]==a[x+1]:
                bad-=1
            a[x]='?'
            if x>0 and a[x-1]==a[x] and a[x-1]!='?':
                bad+=1
            if x<n-1 and a[x]==a[x+1] and a[x+1]!='?':
                bad+=1
            if bad==0:
                return i+1
