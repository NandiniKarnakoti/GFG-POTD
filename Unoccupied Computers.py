# Problem: Unoccupied Computers
# Difficulty: Easy
# Date: 2 September 2026

"""
Problem:
A cafe has n computers and customer events are represented
by a string of uppercase letters.

Each distinct letter appears exactly twice:
- First occurrence → Customer arrives
- Second occurrence → Customer leaves

If no computer is available when a customer arrives,
that customer is rejected.

Return the number of rejected customers.
"""

# ---------------------------------------------------
# Approach: Simulation using Sets
# Time Complexity: O(|S|)
# Space Complexity: O(26)
# ---------------------------------------------------

class Solution:
    def solve(self, n, s):
        # code here
        active = set()
        rejected = set()
        count = 0
        for ch in s:
            if ch in active:
                active.remove(ch)
            elif ch in rejected:
                rejected.remove(ch)
            else:
                if len(active) < n:
                    active.add(ch)
                else:
                    rejected.add(ch)
                    count += 1
        return count
        
