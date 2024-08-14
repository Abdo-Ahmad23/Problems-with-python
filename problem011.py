class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        sum1=''
        sum2=''
        for i in word1:
            sum1+=i
        for i in word2:
            sum2+=i
        if sum1==sum2:
            return True
        else:
            return False