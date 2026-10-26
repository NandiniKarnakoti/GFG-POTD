# Problem: Sum of Beauty of All Substrings
# Difficulty: Easy
# Date: 25 October 2026

"""
Problem:
Calculate the sum of the beauty of every substring of s.
The beauty of a substring is the difference between the maximum
and minimum frequencies of its characters.
"""

# ---------------------------------------------------
# Approach: Frequency Counting
# Time Complexity: O(N^2 * 26) = O(N^2)
# Space Complexity: O(26) = O(1)
# ---------------------------------------------------

class Solution:
    def beautySum(self, s: str) -> int:
        # code here 
        n=len(s)
        ans=0
        for i in range(n):
            freq=[0]*26
            max_freq=0
            for j in range(i,n):
                idx=ord(s[j])-97
                freq[idx]+=1
                max_freq=max(max_freq,freq[idx])
                min_freq=n
                for f in freq:
                    if f>0:
                        min_freq=min(min_freq,f)
                ans+=max_freq-min_freq
        return ans
