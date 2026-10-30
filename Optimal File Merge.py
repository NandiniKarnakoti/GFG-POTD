# Problem: Optimal File Merge
# Difficulty: Medium
# Date: 29 October 2026

"""
Problem:
Given an array where each element represents a file size, merge all
files into one file with minimum total computation cost.
Merging two files costs the sum of their sizes.
"""

# ---------------------------------------------------
# Approach: Greedy + Min Heap
# Time Complexity: O(N log N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def minComputation(self, files):
        # code here
        import heapq
        heapq.heapify(files)
        total_cost=0
        while len(files)>1:
            first=heapq.heappop(files)
            second=heapq.heappop(files)
            merged=first+second
            total_cost+=merged
            heapq.heappush(files,merged)
        return total_cost
