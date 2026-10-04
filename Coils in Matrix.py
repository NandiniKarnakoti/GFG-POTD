# Problem: Coils in Matrix
# Difficulty: Medium
# Date: 3 October 2026

"""
Problem:
Given a positive integer n, form a 4n x 4n matrix containing values from
1 to (4n)^2 in row-major order.

Construct two coils:
1. The first coil starts from the top-left cell and spirals inward.
2. The second coil starts from the bottom-right cell and spirals inward
   in the opposite direction.

Return both coils in their required order.
"""

# ---------------------------------------------------
# Approach: Layer-by-Layer Spiral Traversal
# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
# ---------------------------------------------------

class Solution:
    def formCoils(self, n: int) -> list[list[int]]:
        # code here
        m=4*n
        c1=[]
        x=0
        while x<m:
            for r in range(x,m-x):
                c1.append(r*m+x+1)
            for c in range(x+1,m-x-1):
                c1.append((m-x-1)*m+c+1)
            for r in range(m-x-2,x,-1):
                c1.append(r*m+(m-x-2)+1)
            for c in range(m-x-3,x+1,-1):
                c1.append((x+1)*m+c+1)
            x+=2
        c2=[m*m-v+1 for v in c1]
        return [c1,c2]
