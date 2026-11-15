# Problem: Max Equal Sum in 3 Stacks
# Difficulty: Medium
# Date: 14 November 2026

"""
Problem:
Given three stacks represented by arrays, where the first
element is the top, find the maximum equal sum possible
by removing zero or more elements from the tops.

Return 0 if equal sums cannot be achieved.
"""

# ---------------------------------------------------
# Approach: Greedy + Three Pointers
# Time Complexity: O(N1 + N2 + N3)
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def maxEqualSum(self, s1: list[int], s2: list[int], s3: list[int]) -> int:
        # code here
        sum1=sum(s1)
        sum2=sum(s2)
        sum3=sum(s3)
        i=j=k=0
        while i<len(s1) and j<len(s2) and k<len(s3):
            if sum1==sum2==sum3:
                return sum1
            if sum1>=sum2 and sum1>=sum3:
                sum1-=s1[i]
                i+=1
            elif sum2>=sum1 and sum2>=sum3:
                sum2-=s2[j]
                j+=1
            else:
                sum3-=s3[k]
                k+=1
        if sum1==sum2==sum3:
            return sum1
        return 0

        
