class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_str = ""
        for c in s:
            if c.isalnum():
                clean_str += c

        s1 = clean_str.replace(" ", "")
        s2 = s1.lower()

        reversed_str = s2.strip()[::-1]

        return s2.strip()  == reversed_str
        