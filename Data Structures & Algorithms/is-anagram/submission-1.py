import string 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ascii_lower = {char: 0 for char in string.ascii_lowercase}
        for c in s:
            ascii_lower[c] += 1
        for c in t:
            ascii_lower[c] -= 1
        
        for i in ascii_lower.values():
            if i != 0:
                return False
        return True
