# Problem: Range Vowel Count Queries
# Difficulty: Medium
# Date: 26 November 2026
# Language: Python

"""
Problem:
Given a string and multiple range queries, count the
number of vowels in each substring s[l...r].
"""

# ---------------------------------------------------
# Approach: Prefix Sum
# Time Complexity: O(n + q)
# Space Complexity: O(n)
# ---------------------------------------------------

class Solution:
    def countVowels(self, s: str, queries: list[list[int]]) -> list[int]:
        # code here
        n=len(s)
        vowels={'a','e','i','o','u'}
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i]+(s[i] in vowels)
        ans=[]
        for l,r in queries:
            ans.append(prefix[r+1]-prefix[l])
        return ans
