# Problem: Count Group Occurrences
# Difficulty: Easy
# Date: 9 November 2026

"""
Problem:
Given a string s and an integer k, count the number of
distinct characters that appear in exactly k groups.

A group consists of one or more consecutive occurrences
of the same character.
"""

# ---------------------------------------------------
# Approach: Single Traversal + Hash Map
# Time Complexity: O(N)
# Space Complexity: O(1) - at most 26 lowercase characters
# ---------------------------------------------------

class Solution:
    def getCount (self, s, k):
        # code here
        freq={}
        prev=''
        for ch in s:
            if ch!=prev:
                freq[ch]=freq.get(ch,0)+1
                prev=ch
        return sum(1 for v in freq.values() if v==k)
