# Problem: Count Pairs Divisible By K 
# Difficulty: Medium 
# Date: 9 July 2026

""" 
Problem:
Count the number of pairs in the array 
whose sum is divisible by k.
"""
# --------------------------------------------------- 
# Approach: Frequency of Remainders 
# Time Complexity: O(N) 
# Space Complexity: O(K) 
# ---------------------------------------------------

class Solution:
    def countKdivPairs(self, arr, k):
        # code here
        freq = [0] * k
        ans = 0
        for num in arr:
            rem = num % k
            ans += freq[(k - rem) % k]
            freq[rem] += 1
        return ans
        
