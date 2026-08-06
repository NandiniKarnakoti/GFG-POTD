# Problem: Subarrays with Sum in Range
# Difficulty: Hard
# Date: 5 August 2026

"""
Problem:
Given an array and two integers l and r,
count the number of subarrays whose sum
lies in the inclusive range [l, r].
"""

# ---------------------------------------------------
# Approach: Sliding Window
# Time Complexity: O(N)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def countSubarray(self, arr: list[int], l: int, r: int) -> int:
        # code here
        def count(k):
            left = 0
            curr_sum = 0
            ans = 0
            for right in range(len(arr)):
                curr_sum += arr[right]
                while curr_sum > k:
                    curr_sum -= arr[left]
                    left += 1
                ans += right - left + 1
            return ans
        return count(r) - count(l - 1)
        
