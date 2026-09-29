# Problem: Range GCD Queries
# Difficulty: Medium
# Date: 28 September 2026

"""
Problem:
Given an integer array arr[] and queries of two types:

Type 1: [0, l, r] -> Find the GCD of all elements in arr[l...r].
Type 2: [1, index, value] -> Update arr[index] to value.

Return the answers for all Type 1 queries.
"""

# ---------------------------------------------------
# Approach: Segment Tree
# Time Complexity: O(N + Q log N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def processQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        # code here
        from math import gcd
        n = len(arr)
        seg = [0] * (4 * n)
        def build(node, start, end):
            if start == end:
                seg[node] = arr[start]
                return
            mid = (start + end) // 2
            build(node * 2, start, mid)
            build(node * 2 + 1, mid + 1, end)
            seg[node] = gcd(seg[node * 2], seg[node * 2 + 1])
        def update(node, start, end, index, value):
            if start == end:
                seg[node] = value
                return
            mid = (start + end) // 2
            if index <= mid:
                update(node * 2, start, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, end, index, value)
            seg[node] = gcd(seg[node * 2], seg[node * 2 + 1])
        def query(node, start, end, left, right):
            if right < start or end < left:
                return 0
            if left <= start and end <= right:
                return seg[node]
            mid = (start + end) // 2
            return gcd(query(node * 2, start, mid, left, right), query(node * 2 + 1, mid + 1, end, left, right))
        build(1, 0, n - 1)
        ans = []
        for q in queries:
            if q[0] == 0:
                ans.append(query(1, 0, n - 1, q[1], q[2]))
            else:
                arr[q[1]] = q[2]
                update(1, 0, n - 1, q[1], q[2])
        return ans
