# Problem: Transform String
# Difficulty: Medium
# Language: Python

"""
Problem:
Find the minimum number of steps required to transform
string s1 into string s2.

The allowed operation is selecting a character from s1
and inserting it at the beginning of the string.

Return -1 if transformation is not possible.
"""

# ---------------------------------------------------
# Approach: Frequency Check + Reverse Traversal
# Time Complexity: O(N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def transform(self, s1, s2): 
        #code here
        if len(s1)!=len(s2):
            return -1
        freq={}
        for ch in s1:
            freq[ch]=freq.get(ch,0)+1
        for ch in s2:
            freq[ch]=freq.get(ch,0)-1
        for value in freq.values():
            if value!=0:
                return -1
        i=len(s1)-1
        j=len(s2)-1
        count=0
        while i>=0:
            if s1[i]==s2[j]:
                j-=1
            else:
                count+=1
            i-=1
        return count
