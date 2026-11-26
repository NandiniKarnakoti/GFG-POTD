# Problem: Geek's Destination with Special Jump
# Difficulty: Hard
# Date: 25 November 2026
# Language: Python

"""
Problem:
Find the sum of minimum times required to reach or pass
destination d for every jump length j in [l, r].
"""

# ---------------------------------------------------
# Approach: Binary Search + Prefix Sum
# Time Complexity: O(log d)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def minTime(self, a: int, b: int, d: int, l: int, r: int) -> int:
        # code here
        MOD=10**9+7
        c=a-b
        def time(x):
            if x<=a:
                return x
            k=(x-a+c-1)//c
            return x+2*b*k
        def prefix(n):
            if n<=0:
                return 0
            if n<=a:
                return n*(n+1)//2
            total=a*(a+1)//2
            total+=(n*(n+1)-a*(a+1))//2
            m=n-a
            q,rem=divmod(m,c)
            s=c*q*(q+1)//2+rem*(q+1)
            total+=2*b*s
            return total
        L,R=d-r,d-l
        normal=time(d)
        low,high=L,R
        p=L-1
        while low<=high:
            mid=(low+high)//2
            if time(mid)+1<=normal:
                p=mid
                low=mid+1
            else:
                high=mid-1
        ans=0
        if p>=L:
            ans+=prefix(p)-prefix(L-1)
            ans+=p-L+1
        ans+=(R-max(L,p+1)+1)*normal
        return ans%MOD
