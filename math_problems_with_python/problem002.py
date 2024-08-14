class Solution:
    def is_palindrome(s):
        s = s.lower().replace(" ", "")
        return s == s[::-1]
    def isStrictlyPalindromic(self, n: int) -> bool:
        if n==4 and Solution.is_palindrome(bin(n)[2:]):
            return True
        else:
            return False