# Problem: Minimum Multiplications to Reach End 
# Difficulty: Medium 
# Date: 20 May 2026
#Language: Python

"""
Problem:
Given a start value and an end value, in one operation
you can multiply the current value by any element from 
the array and take modulo 1000.

Return the minimum number of steps required to reach
the end value. If not possible, return -1.
"""

class Solution:
    def isProduct(self, arr, target):
        # code here
        arr.sort()
        l,r=0,len(arr)-1
        while l<r:
            res=arr[l]*arr[r]
            if res==target:
                return True
            elif res<target:
                l+=1
            else:
                r-=1
        return False
