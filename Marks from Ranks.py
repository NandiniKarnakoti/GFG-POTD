# Problem: Marks from Ranks
# Difficulty: Medium
# Date: 30 August 2026

"""
Problem:
Given non-overlapping intervals [l[i], r[i]] representing
valid marks, find the mark corresponding to each given rank.

The intervals are sorted in increasing order.
The smallest valid mark has rank 1.
"""

# ---------------------------------------------------
# Approach: Prefix Sum + Binary Search
# Time Complexity: O(N + Q log N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:

    def getMarks(self, l, r, rank):
        """code here"""
        prefix=[]
        total=0
        for i in range(len(l)):
            total+=r[i]-l[i]+1
            prefix.append(total)
        ans=[]
        for k in rank:
            left=0
            right=len(prefix)-1
            while left<=right:
                mid=(left+right)//2
                if prefix[mid]>=k:
                    right=mid-1
                else:
                    left=mid+1
            prev=prefix[left-1] if left>0 else 0
            ans.append(l[left]+k-prev-1)
        return ans
