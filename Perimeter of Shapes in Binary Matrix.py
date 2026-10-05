# Problem: Perimeter of Shapes in Binary Matrix
# Difficulty: Easy
# Date: 4 October 2026

"""
Problem:
Given a binary matrix mat[][], find the total perimeter of all figures
formed by cells containing 1s.

Each cell containing 1 contributes one unit of perimeter for every side
that is either on the boundary of the matrix or adjacent to a cell
containing 0.
"""

# ---------------------------------------------------
# Approach: Boundary and Neighbor Checking
# Time Complexity: O(N * M)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def findPerimeter(self, mat: List[List[int]]) -> int:
        # code here
        n=len(mat)
        m=len(mat[0])
        perimeter=0
        for i in range(n):
            for j in range(m):
                if mat[i][j]==1:
                    if i==0 or mat[i-1][j]==0:
                        perimeter+=1
                    if i==n-1 or mat[i+1][j]==0:
                        perimeter+=1
                    if j==0 or mat[i][j-1]==0:
                        perimeter+=1
                    if j==m-1 or mat[i][j+1]==0:
                        perimeter+=1
        return perimeter
        
