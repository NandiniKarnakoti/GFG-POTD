# Problem: Rearrange the Array
# Difficulty: Hard
# Date: 12 July 2026

"""
Problem:
Given a permutation b[], each operation moves the
element at position i to position b[i].

Find the minimum number of operations required
for all elements to return to their original
positions simultaneously.
"""

# ---------------------------------------------------
# Approach: Cycle Decomposition + LCM
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def minOperations(self, b):
        # code here
        import math
        MOD = 10**9 + 7
        n = len(b)
        vis = [False] * n
        ans = 1
        for i in range(n):
            if not vis[i]:
                cnt = 0
                j = i
                while not vis[j]:
                    vis[j] = True
                    j = b[j] - 1   
                    cnt += 1
                ans = (ans // math.gcd(ans, cnt)) * cnt
        return ans % MOD
        
