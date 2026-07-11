class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        seen = [] 
        if len(s) != len(t): 
            return False 
        
        for char in s:

            seen.append(char)
        
        for char_t in t: 
            if char_t in seen: 
                seen.remove(char_t)
            else:
                return False
        
        return True
        