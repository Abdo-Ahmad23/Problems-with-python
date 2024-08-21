import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input().split()
tmp=''
for i in s:
    if i.count('-')==0:
        tmp+='5'
    elif i.count('-')==1:
        if i[0]=='-':
            tmp+='6'
        else:
            tmp+='4'
    elif i.count('-')==2:
        if i[0]=='-':
            tmp+='7'
        else:
            tmp+='3'
    elif i.count('-')==3:
        if i[0]=='-':
            tmp+='8'
        else:
            tmp+='2'
    elif i.count('-')==4:
        if i[0]=='-':
            tmp+='9'
        else:
            tmp+='1'
    else:
        tmp+='0'
print(int(tmp))

