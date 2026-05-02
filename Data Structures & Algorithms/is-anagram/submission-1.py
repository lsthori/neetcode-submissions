class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        char_list = list(s)

        for char in t:
            if char in char_list:
                char_list.remove(char)

        return True if len(char_list) == 0 else False 

        