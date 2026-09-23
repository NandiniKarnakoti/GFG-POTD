# Problem: Longest Matching in Dictionary with Removals
# Difficulty: Medium
# Date: 22 September 2026

"""
Problem:
Given a string s and a dictionary d[], find the longest word
in the dictionary that can be obtained by deleting characters
from s without changing the order of the remaining characters.

If multiple words have the same maximum length, return the
lexicographically smallest word.

Return an empty string if no valid word exists.
"""

# ---------------------------------------------------
# Approach: Character Position Lists + Binary Search
# Time Complexity: O(|s| + Σ |word| log |s|)
# Space Complexity: O(|s|)
# ---------------------------------------------------

class Solution:
    def findLongestWord(self, s: str, d: list) -> str:
        # code here
        from bisect import bisect_right
        pos = [[] for _ in range(26)]
        for i, ch in enumerate(s):
            pos[ord(ch) - ord('a')].append(i)
        ans = ""
        for word in d:
            prev = -1
            valid = True
            for ch in word:
                arr = pos[ord(ch) - ord('a')]
                idx = bisect_right(arr, prev)
                if idx == len(arr):
                    valid = False
                    break
                prev = arr[idx]
            if valid:
                if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                    ans = word
        return ans
