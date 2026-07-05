# Problem: Substrings with more 1's than 0's 
# Difficulty: Hard 
# Date: 4 July 2026

""" 
Problem:
Count the number of substrings having
more 1's than 0's. 
"""

# ---------------------------------------------------
# Approach: Prefix Sum + Fenwick Tree (BIT)
# Time Complexity: O(N log N) 
# Space Complexity: O(N) 
# ---------------------------------------------------

class Solution:
    def countSubstring(self, s):
        # code here
        n = len(s)
        prefix = [0]
        cur = 0
        for ch in s:
            if ch == '1':
                cur += 1
            else:
                cur -= 1
            prefix.append(cur)
        vals = sorted(set(prefix))
        rank = {v: i + 1 for i, v in enumerate(vals)}
        m = len(vals)
        bit = [0] * (m + 1)
        def update(i):
            while i <= m:
                bit[i] += 1
                i += i & -i
        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res
        ans = 0
        for x in prefix:
            idx = rank[x]
            ans += query(idx - 1)
            update(idx)
        return ans
