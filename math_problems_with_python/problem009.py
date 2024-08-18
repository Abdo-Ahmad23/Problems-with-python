class Solution:
    def countDigits(self, num: int) -> int:
        cnt=0
        for i in str(num):
            cnt+=(1 if num%int(i)==0 else 0)
        return cnt