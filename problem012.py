class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        list_tuple=list()
        for i in range(len(names)):
            t=(heights[i],names[i])
            list_tuple.append(t)
        list_tuple=sorted(list_tuple,reverse=True)
        for i in range(len(list_tuple)):
            names[i]=list_tuple[i][1]
        return names