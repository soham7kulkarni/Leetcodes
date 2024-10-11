# egg - add
# egg - aaa
# when we use only one hashmap from s to t
# we want to check if t to s is valid after s to t, 
# we have to go through VALUES of smap, O(n)
# hence use both hashmap s to t and t to s
# if we use single hashmap eggd - addm fails 
# even though it is true bcoz we say g-to-d and d-to-g, so m-to-d not allowed. Which is not true 
# Now TC - O(n), space - O(1)
# if we use smap and then just check if value has already been mapped or not, 
# we can use hashset, making it O(1) for both
# Approach - check if s is mapped to t, if yes, check value, 
# if no, check if t is already mapped to anything by checking hashset, 
# if yes, fails, if no then only map s to t


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashset = set()
        hashmap = {}
        if len(s) != len(t): return False
        if s == "" and t == "": return True
        for s_char, t_char in zip(s,t):
            if s_char not in hashmap:
                if t_char not in hashset:
                    hashmap[s_char] = t_char
                    hashset.add(t_char)
                else:
                    return False
            else:
                if hashmap[s_char] != t_char: return False
        return True
        