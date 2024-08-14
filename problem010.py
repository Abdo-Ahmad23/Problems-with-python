class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        s = sentences
        mx = 0
        for i in s:
            my_list = i.split()
            mx = max(mx, len(my_list))
        return mx
