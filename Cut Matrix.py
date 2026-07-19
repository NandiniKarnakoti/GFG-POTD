# Problem: Cut Matrix
# Difficulty: Hard
# Date: 17 July 2026

"""
Problem:
Given a binary matrix and an integer k,
count the number of ways to divide the matrix
into k pieces such that each piece contains
at least one 1.

Only the bottom part after a horizontal cut
or the right part after a vertical cut can
be further divided.
"""

# ---------------------------------------------------
# Approach: Suffix Sum + DP + Prefix Suffix Optimization
# Time Complexity: O(K × N × M)
# Space Complexity: O(N × M)
# ---------------------------------------------------

class Solution:
    def findWays(self, matrix, k):
        # code here
        MOD=10**9+7
        rows=len(matrix)
        cols=len(matrix[0])
        suffix=[[0]*(cols+1) for _ in range(rows+1)]
        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                suffix[r][c]=matrix[r][c]+suffix[r+1][c]+suffix[r][c+1]-suffix[r+1][c+1]
        if suffix[0][0]<k:
            return 0
        nextRow=[[rows]*cols for _ in range(rows)]
        for c in range(cols):
            for r in range(rows-1,-1,-1):
                if r+1<rows and suffix[r][c]>suffix[r+1][c]:
                    nextRow[r][c]=r+1
                elif r+1<rows:
                    nextRow[r][c]=nextRow[r+1][c]
        nextCol=[[cols]*cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols-1,-1,-1):
                if c+1<cols and suffix[r][c]>suffix[r][c+1]:
                    nextCol[r][c]=c+1
                elif c+1<cols:
                    nextCol[r][c]=nextCol[r][c+1]
        dp=[[0]*cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if suffix[r][c]:
                    dp[r][c]=1
        for pieces in range(2,k+1):
            rowSuffix=[[0]*(cols+1) for _ in range(rows+1)]
            colSuffix=[[0]*(cols+1) for _ in range(rows+1)]
            for r in range(rows-1,-1,-1):
                for c in range(cols-1,-1,-1):
                    rowSuffix[r][c]=(rowSuffix[r+1][c]+dp[r][c])%MOD
                    colSuffix[r][c]=(colSuffix[r][c+1]+dp[r][c])%MOD
            cur=[[0]*cols for _ in range(rows)]
            for r in range(rows):
                for c in range(cols):
                    if suffix[r][c]<pieces:
                        continue
                    ways=0
                    if nextRow[r][c]<rows:
                        ways+=rowSuffix[nextRow[r][c]][c]
                    if nextCol[r][c]<cols:
                        ways+=colSuffix[r][nextCol[r][c]]
                    cur[r][c]=ways%MOD
            dp=cur
        return dp[0][0]
