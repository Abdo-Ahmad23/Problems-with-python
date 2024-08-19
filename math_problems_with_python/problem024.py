import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
tmp=''
for i in s:
    if i.isupper():
        tmp+=str(ord(i)-ord('A')+1)
    elif i.islower():
        tmp+=str(ord(i)-ord('a')+1)
    else:
        tmp+=i
print(tmp)
