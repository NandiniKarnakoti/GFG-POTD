# Problem: Your Social Network
# Difficulty: Medium
# Date: 5 October 2026

"""
Problem:
Given the friend of each user from 2 to n, find all users that can be
reached by repeatedly following the friend links.

For every reachable pair [i, j], store:
[i, j, k] where k is the number of links required to reach j from i.

The result is ordered by starting user and then by increasing reachable
user number.
"""

# ---------------------------------------------------
# Approach: Friend Chain Traversal
# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
# ---------------------------------------------------

class Solution:
    def socialNetwork(self, arr):
        # code here
        n = len(arr) + 1
        result = []
        for i in range(2, n + 1):
            current = arr[i - 2]
            distance = 1
            temp = []
            while True:
                temp.append([i, current, distance])
                if current == 1:
                    break
                current = arr[current - 2]
                distance += 1
            temp.reverse()
            result.extend(temp)
        return result
