# Problem: Check Subset Sum Divisible by K 
# Difficulty: Medium 
# Date: 2 July 2026

""" 
Problem: 
Determine whether there exists a non-empty subset
whose sum is divisible by k. 
"""

# --------------------------------------------------- 
# Approach: DP on Remainders 
# Time Complexity: O(N × K) 
# Space Complexity: O(K) 
# ---------------------------------------------------

class Solution:
    def divisibleByK(self, arr, k):
        # code here
        dp = [False] * k
        for num in arr:
            new_dp = dp[:]
            new_dp[num % k] = True
            for r in range(k):
                if dp[r]:
                    new_dp[(r + num) % k] = True
            dp = new_dp
            if dp[0]:
                return True
        return False
        
