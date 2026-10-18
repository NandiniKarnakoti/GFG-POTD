# Problem: Convert One String to Another with Constraints
# Difficulty: Easy
# Date: 17 October 2026

"""
Problem:
Given two strings s1 and s2 containing only 'A', 'B', and '#',
determine whether s1 can be transformed into s2.

Rules:
1. 'A' can move only towards the left.
2. 'B' can move only towards the right.
3. 'A' and 'B' cannot cross each other.
4. '#' represents an empty position.
"""

# ---------------------------------------------------
# Approach: Two Pointers + Position Validation
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def isItPossible(self, s1: str, s2: str) -> bool:
        # code here
        if s1.replace('#','')!=s2.replace('#',''):
            return False
        i=j=0
        n=len(s1)
        while i<n and j<n:
            while i<n and s1[i]=='#':
                i+=1
            while j<n and s2[j]=='#':
                j+=1
            if i==n or j==n:
                return i==n and j==n
            if s1[i]=='A' and i<j:
                return False
            if s1[i]=='B' and i>j:
                return False
            i+=1
            j+=1
        return True

        
