class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        sum=0
        for i in range(len(operations)):
            if '+' in operations[i]:
                sum+=1
            else:
                sum-=1
        return sum