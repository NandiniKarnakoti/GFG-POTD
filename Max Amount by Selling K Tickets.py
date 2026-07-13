# Problem: Max Amount by Selling K Tickets
# Difficulty: Medium
# Date: 12 July 2026

"""
Problem:
Given the number of tickets available with each seller,
find the maximum amount that can be earned by selling
at most k tickets.

The price of a ticket equals the number of tickets
remaining with that seller at the time of sale.
"""

#---------------------------------------------------
# Approach: Max Heap (Priority Queue)
# Time Complexity: O(K log N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def maxAmount(self, arr, k):
        # code here
        import heapq
        MOD = 10**9 + 7
        heap = [-x for x in arr]
        heapq.heapify(heap)
        ans = 0
        while k > 0 and heap:
            cur = -heapq.heappop(heap)
            ans = (ans + cur) % MOD
            if cur > 1:
                heapq.heappush(heap, -(cur - 1))
            k -= 1
        return ans
        
