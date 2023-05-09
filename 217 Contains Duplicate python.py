class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = dict()
        for i in nums:
            if i in s:
                return True
            else:
                s[i] = 1 # any flag can work here
        return False
""" 
Hashtable comprises of a hash function and an array. The hashed result(must be a number) is the index of the array. 
Whenever you want to see if something already exist, hash it then go direct to the position. So the lookup is O(1).
Python dictionary is actually a hashtable.
"""