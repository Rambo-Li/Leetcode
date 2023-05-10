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
Hashtable comprises a hash function and an array. The hashed result(must be a number) is the index of the array. 
Whenever you want to see if something already exists, hash it then go direct to the position. So the lookup is O(1).
Python dictionary is actually a hashtable.
"""

""" This is a one-liner if succinctness is what you are after
    return len(set(nums)) != len(nums)
"""

""" Since this problem will give you an array of integers, we actually don't need the hash function. But then you need to 
deal with dynamic size of the array. I tried to allocate a big array at the beginning and time ran out, so it means it has
to be a dynamic array, whose implementation is harder than the problem itself."""
