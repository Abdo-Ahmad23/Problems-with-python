class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        my_list=list()
        my_list.append(celsius+273.15)
        my_list.append(celsius*1.80+32.00)
        return my_list
    