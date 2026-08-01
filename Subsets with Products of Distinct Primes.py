# Problem: Subsets with Products of Distinct Primes
# Difficulty: Hard
# Date: 31 July 2026

"""
Problem:
Given an array, count the number of subsets whose
product can be represented as a product of one or
more distinct prime numbers.

Return the count modulo 1e9+7.
"""

# ---------------------------------------------------
# Approach: Bitmask DP
# Time Complexity: O(N + 30 × 2^10)
# Space Complexity: O(2^10)
# ---------------------------------------------------

class Solution:
    def countSubsets(self, arr):
        # code here
        MOD = 1000000007
        primes = [2,3,5,7,11,13,17,19,23,29]
        freq = [0]*31
        for x in arr:
            freq[x] += 1
        masks = [0]*31
        for x in range(2,31):
            t = x
            mask = 0
            ok = True
            for i,p in enumerate(primes):
                cnt = 0
                while t % p == 0:
                    t //= p
                    cnt += 1
                if cnt > 1:
                    ok = False
                    break
                if cnt == 1:
                    mask |= 1 << i
            if ok:
                masks[x] = mask
        dp = [0]*1024
        dp[0] = 1
        for x in range(2,31):
            if freq[x] == 0 or masks[x] == 0:
                continue
            m = masks[x]
            ndp = dp[:]
            for mask in range(1024):
                if dp[mask] and (mask & m) == 0:
                    ndp[mask | m] = (ndp[mask | m] + dp[mask] * freq[x]) % MOD
            dp = ndp
        ans = (sum(dp) - 1) % MOD
        ans = ans * pow(2, freq[1], MOD) % MOD
        return ans
