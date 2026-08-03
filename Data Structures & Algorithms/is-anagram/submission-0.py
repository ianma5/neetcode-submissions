class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        s2 = {}

        for char in s:
            if char not in s1:
                s1[char] = 1
            else:
                s1[char] += 1
        
        for char in t:
            if char not in s2:
                s2[char] = 1
            else:
                s2[char] += 1
        
        if s1 == s2: return True
        return False
        