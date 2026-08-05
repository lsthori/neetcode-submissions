class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!= len(t):
            return False

        return sorted(s) == sorted(t)

        # cnt = 0

        # for x in s:
        #     for y in t:
        #         if x == y:
        #             cnt += 1

        # if cnt == len(s):
        #     return true
        # else:
        #     return false

