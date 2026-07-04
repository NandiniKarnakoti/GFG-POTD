# Problem: Ways to Increase LCS by One 
# Difficulty: Medium 
# Date: 3 July 2026

""" 
Problem:
Insert exactly one character into s1 such that
the LCS of s1 and s2 increases by exactly one.
Return the number of valid insertions.
"""

# --------------------------------------------------- 
# Approach: LCS + Reverse LCS Dynamic Programming 
# Time Complexity: O(N × M) 
# Space Complexity: O(N × M) 
# ---------------------------------------------------

class Solution:
    def waysToIncreaseLCSBy1(self, s1, s2):
        # code here
        n, m = len(s1), len(s2)
        pref = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    pref[i][j] = pref[i - 1][j - 1] + 1
                else:
                    pref[i][j] = max(pref[i - 1][j], pref[i][j - 1])
        lcs = pref[n][m]
        suff = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s1[i] == s2[j]:
                    suff[i][j] = 1 + suff[i + 1][j + 1]
                else:
                    suff[i][j] = max(suff[i + 1][j], suff[i][j + 1])
        ans = 0
        for i in range(n + 1):
            chars = set()
            for j in range(m):
                if s2[j] in chars:
                    continue
                if pref[i][j] + 1 + suff[i][j + 1] == lcs + 1:
                    chars.add(s2[j])
            ans += len(chars)
        return ans
