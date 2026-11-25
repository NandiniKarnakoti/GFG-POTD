# Problem: Two Pairs with Same Sum
# Difficulty: Medium
# Date: 24 November 2026
# Language: Python

"""
Problem:
Find four distinct indices a, b, c, d such that
arr[a] + arr[b] = arr[c] + arr[d].

Return the lexicographically smallest valid quadruplet.
If none exists, return [-1, -1, -1, -1].
"""

# ---------------------------------------------------
# Approach: Hash Map + Pair Tracking
# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
# ---------------------------------------------------

class Solution:
    def findPairs(self, arr: list[int]) -> list[int]:
        # code here
        n=len(arr)
        mp={}
        for i in range(n):
            for j in range(i+1,n):
                s=arr[i]+arr[j]
                if s not in mp:
                    mp[s]=[[],{}]
                pairs,deg=mp[s]
                pairs.append((i,j))
                deg[i]=deg.get(i,0)+1
                deg[j]=deg.get(j,0)+1
        ans=None
        for pairs,deg in mp.values():
            m=len(pairs)
            for k,(a,b) in enumerate(pairs):
                if m-deg[a]-deg[b]+1>0:
                    for x in range(k+1,m):
                        c,d=pairs[x]
                        if a!=c and a!=d and b!=c and b!=d:
                            cur=(a,b,c,d)
                            if ans is None or cur<ans:
                                ans=cur
                            break
                    break
        return list(ans) if ans is not None else [-1,-1,-1,-1]
