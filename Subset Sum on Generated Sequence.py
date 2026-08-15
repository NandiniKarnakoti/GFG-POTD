# Problem: Subset Sum on Generated Sequence
# Difficulty: Medium
# Date: 14 August 2026

"""
Problem:
Generate the sequence by starting with s. For every
value arr[i], add arr[i] to the current total and
write the new total on the paper.

Check whether x can be formed as a sum of some of
the generated numbers.
"""

# ---------------------------------------------------
# Approach: Greedy from Largest to Smallest
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def isPossible(self, arr, s, x):
        # code here 
        if x == 0:
            return True
        nums = [s]
        total = s
        for val in arr:
            new_num = total + val
            if new_num > x:
                break
            nums.append(new_num)
            total += new_num
        remaining = x
        for num in reversed(nums):
            if num <= remaining:
                remaining -= num
            if remaining == 0:
                return True
        return False
        
