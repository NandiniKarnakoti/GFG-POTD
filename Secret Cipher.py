# Problem: Secret Cipher
# Difficulty: Hard
# Date: 18 August 2026

"""
Problem:
Given the original string s, find the shortest encrypted
string that decodes to s.

If multiple encrypted strings have the same minimum length,
return the lexicographically smallest one.
"""

# ---------------------------------------------------
# Approach: Z-Algorithm + Dynamic Programming
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def compress(self, s):
        # code here
        n=len(s)
        z=[0]*n
        l=r=0
        for i in range(1,n):
            if i<r:
                z[i]=min(r-i,z[i-l])
            while i+z[i]<n and s[z[i]]==s[i+z[i]]:
                z[i]+=1
            if i+z[i]>r:
                l=i
                r=i+z[i]
        dp=[0]*(n+1)
        choice=['']*(n+1)
        dp[n]=0
        for i in range(n-1,0,-1):
            dp[i]=1+dp[i+1]
            choice[i]=s[i]
            if 2*i<=n and z[i]>=i and 1+dp[2*i]<=dp[i]:
                dp[i]=1+dp[2*i]
                choice[i]='*'
        ans=s[0]
        i=1
        while i<n:
            ans+=choice[i]
            if choice[i]=='*':
                i*=2
            else:
                i+=1
        return ans
