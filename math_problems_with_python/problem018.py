class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if str(num)[-1]=='0' and len(str(num))>1:
            return False
        return True
