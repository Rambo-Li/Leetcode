class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for s in strs:
            temp = "".join(sorted(s)) # this is the uniqueness
            if temp in d:
                d[temp].append(s)
            else:
                d[temp] = [s]

        return d.values()
    
""" The key of hashtable is find the uniqueness of the input. As for a anagram, it could be a sorted version, or it could be a letter count."""
    