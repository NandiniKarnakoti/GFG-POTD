# Problem: Repeated Pattern Check
# Difficulty: Easy
# Date: 17 November 2026

"""
Problem:
Given a string s containing only 'x' and 'y',
check whether it can be formed by concatenating
substrings of the pattern x^n y^n.

Each substring must contain equal numbers of
consecutive 'x' and 'y' characters.
"""

# ---------------------------------------------------
# Approach: Two Pointers + Group Counting
# Time Complexity: O(N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def findPattern(self, s):
        # code here
        i=0
        n=len(s)
        while i<n:
            if s[i]!='x':
                return False
            x=0
            y=0
            while i<n and s[i]=='x':
                x+=1
                i+=1
            while i<n and s[i]=='y':
                y+=1
                i+=1
            if x!=y:
                return False
        return True
