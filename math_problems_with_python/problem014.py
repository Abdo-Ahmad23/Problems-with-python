class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s=''.join(sorted(s,reverse=True))
        return s[1:]+s[0]
