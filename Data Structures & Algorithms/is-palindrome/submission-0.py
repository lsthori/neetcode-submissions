class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_str = ""
        for c in s:
            if c.isalnum():
                clean_str += c

        s1 = clean_str.replace(" ", "")
        s2 = s1.lower()
        easy_str = s2.strip()

        reversed_str = "".join(reversed(easy_str))

        return easy_str  == reversed_str
        