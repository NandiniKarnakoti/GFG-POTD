# Problem: Palindrome with Replacement
# Difficulty: Medium
# Date: 22 October 2026

"""
Problem:
Replace every '?' with a lowercase English letter to form a palindrome.
Return the minimum possible sum of absolute ASCII differences between
adjacent characters, or -1 if forming a palindrome is impossible.
"""

# ---------------------------------------------------
# Approach: Dynamic Programming
# Time Complexity: O(N * 26^2)
# Space Complexity: O(26)
# ---------------------------------------------------

class Solution:
    def minimumSum(self, s: str) -> int:
        # code here
        n=len(s)
        m=(n+1)//2
        a=list(s[:m])
        for i in range(n//2):
            j=n-1-i
            if s[i]!='?' and s[j]!='?' and s[i]!=s[j]:
                return -1
            if s[i]!='?':
                a[i]=s[i]
            elif s[j]!='?':
                a[i]=s[j]
        inf=10**9
        dp=[inf]*26
        for c in range(26):
            if a[0]=='?' or ord(a[0])-97==c:
                dp[c]=0
        for i in range(1,m):
            ndp=[inf]*26
            for c in range(26):
                if a[i]!='?' and ord(a[i])-97!=c:
                    continue
                for p in range(26):
                    ndp[c]=min(ndp[c],dp[p]+abs(p-c))
            dp=ndp
        if n%2==1:
            c=n//2
            if s[c]!='?':
                k=ord(s[c])-97
                dp=[v+abs(i-k) for i,v in enumerate(dp)]
            else:
                dp=[min(dp[p]+abs(p-i) for p in range(26)) for i in range(26)]
        return 2*min(dp)
