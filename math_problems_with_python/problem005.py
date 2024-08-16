class Solution:
    def minimumSum(self, num: int) -> int:
        # 01234
        #  24    3
        s=str(num)
        if len(s)==1:
            return num
        s=sorted(s)
        n1=''
        n2=''
        # return s
        for i in range(1,len(s)+1,1):
            if i%2:
                n1=s[-1*i]+n1
            else:
                n2=s[-1*i]+n2
        return int(n1)+int(n2)


sol=Solution()
print(sol.minimumSum(2932))
