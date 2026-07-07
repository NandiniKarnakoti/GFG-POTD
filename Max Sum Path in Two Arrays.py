# Problem: Max Sum Path in Two Arrays 
# Difficulty: Medium 
# Date: 6 July 2026

""" 
Problem:
Find the maximum sum path from the beginning
of either array to the end of either array. 

You may switch arrays only at common elements. 
"""

# --------------------------------------------------- 
# Approach: Two Pointers 
# Time Complexity: O(N + M) 
# Space Complexity: O(1) 
# ---------------------------------------------------

class Solution:
    def maxPathSum(self, a, b):
        # Code here
        i = j = 0
        sum1 = sum2 = 0
        ans = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                sum1 += a[i]
                i += 1
            elif a[i] > b[j]:
                sum2 += b[j]
                j += 1
            else:
                ans += max(sum1, sum2) + a[i]
                sum1 = sum2 = 0
                i += 1
                j += 1
        while i < len(a):
            sum1 += a[i]
            i += 1
        while j < len(b):
            sum2 += b[j]
            j += 1
        ans += max(sum1, sum2)
        return ans
