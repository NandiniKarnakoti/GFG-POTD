# Problem: Largest Odd Squares with Limited 1s
# Difficulty: Medium
# Date: 11 August 2026

"""
Problem:
For each query, find the largest odd-sized square
centered at the given cell containing at most k ones.

The square must remain completely inside the matrix.
"""

# ---------------------------------------------------
# Approach: 2D Prefix Sum + Binary Search
# Time Complexity: O(N*M + Q*log(min(N,M)))
# Space Complexity: O(N*M)
# ---------------------------------------------------

class Solution:
    def largestSquare(self, mat: list[list[int]], queries: list[list[int]], k: int) -> list[int]:
        # code here
        n=len(mat)
        m=len(mat[0])
        p=[[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                p[i+1][j+1]=mat[i][j]+p[i][j+1]+p[i+1][j]-p[i][j]
        def sm(r1,c1,r2,c2):
            return p[r2+1][c2+1]-p[r1][c2+1]-p[r2+1][c1]+p[r1][c1]
        ans=[]
        for i,j in queries:
            mx=min(i,j,n-1-i,m-1-j)
            if mat[i][j]>k:
                ans.append(-1)
                continue
            l,h,b=0,mx,0
            while l<=h:
                x=(l+h)//2
                if sm(i-x,j-x,i+x,j+x)<=k:
                    b=x
                    l=x+1
                else:
                    h=x-1
            ans.append(2*b+1)
        return ans
        
