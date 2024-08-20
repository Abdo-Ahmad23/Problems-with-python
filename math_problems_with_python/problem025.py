class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums=list()
        for i in range(left,right+1):
            ok=1
            for j in str(i):
                if j!='0' and i % int(j):
                    ok=0
                    break
                if j=='0':
                    ok=0
            if ok:
                nums.append(i)
        return nums
