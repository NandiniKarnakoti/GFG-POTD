# Problem: Generate Usernames
# Difficulty: Easy
# Date: 7 November 2026

"""
Problem:
Given an array of usernames, generate a unique username
for each entry while preserving the original order.

All usernames in the input are initially reserved.
If a username is already used, append the smallest positive
integer suffix that is neither reserved nor already assigned.
"""

# ---------------------------------------------------
# Approach: Hash Sets + Frequency Tracking
# Time Complexity: O(N * K) average, where K is the
#                  number of suffixes checked
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def generateUsernames(self, arr: list[str]) -> list[str]:
        # code here
        reserved=set(arr)
        used=set()
        count={}
        ans=[]
        for name in arr:
            if name not in used:
                ans.append(name)
                used.add(name)
                count[name]=1
            else:
                i=count.get(name,1)
                while name+str(i) in reserved or name+str(i) in used:
                    i+=1
                new=name+str(i)
                ans.append(new)
                used.add(new)
                count[name]=i+1
        return ans
        
