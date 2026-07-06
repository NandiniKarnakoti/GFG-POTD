# Problem: Max Gap Between Two Same 
# Difficulty: Easy 
# Date: 4 July 2026

""" 
Problem:
Find the maximum number of characters 
between any two identical characters.

Return -1 if no character repeats. 
""" 

# ---------------------------------------------------
# Approach: Hash Map (First Occurrence)
# Time Complexity: O(N) 
# Space Complexity: O(26) 
# ---------------------------------------------------

class Solution:
    def maxCharGap(self, s: str) -> int:
        # code here
        first = {}
        ans = -1
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            else:
                ans = max(ans, i - first[ch] - 1)
        return ans

