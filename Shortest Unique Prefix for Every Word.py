# Problem: Shortest Unique Prefix for Every Word
# Difficulty: Hard
# Date: 20 July 2026

"""
Problem:
Given an array of strings, find the shortest
prefix of each string that uniquely identifies
it among all the strings.

It is guaranteed that no string is a prefix
of another string.
"""

# ---------------------------------------------------
# Approach: Trie + Prefix Frequency
# Time Complexity: O(T)
# Space Complexity: O(T)
# ---------------------------------------------------

class TrieNode:
    def __init__(self):
        self.child = {}
        self.count = 0
class Solution:
    def findPrefixes(self, arr):
        root = TrieNode()
        for word in arr:
            node = root
            for ch in word:
                if ch not in node.child:
                    node.child[ch] = TrieNode()
                node = node.child[ch]
                node.count += 1
        ans = []
        for word in arr:
            node = root
            prefix = ""
            for ch in word:
                node = node.child[ch]
                prefix += ch
                if node.count == 1:
                    break
            ans.append(prefix)
        return ans
