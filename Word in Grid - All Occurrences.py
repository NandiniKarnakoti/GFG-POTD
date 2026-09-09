# Problem: Word in Grid - All Occurrences
# Difficulty: Medium
# Date: 8 September 2026

"""
Problem:
Given a 2D grid of characters and a word, find all starting
positions where the word occurs in the grid.

The word can be formed by moving in any of the 8 directions
in a straight line without changing direction.
"""

# ---------------------------------------------------
# Approach: Direction Simulation
# Time Complexity: O(N * M * 8 * L)
# Space Complexity: O(1) excluding output
# ---------------------------------------------------

class Solution:
    def searchWord(self, mat, word):
        # code here
        n=len(mat)
        m=len(mat[0])
        ans=[]
        directions=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for i in range(n):
            for j in range(m):
                if mat[i][j]!=word[0]:
                    continue
                for dx,dy in directions:
                    x,y=i,j
                    k=0
                    while k<len(word):
                        if x<0 or x>=n or y<0 or y>=m or mat[x][y]!=word[k]:
                            break
                        x+=dx
                        y+=dy
                        k+=1
                    if k==len(word):
                        ans.append([i,j])
                        break
        return ans
