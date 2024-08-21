import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
tmp=''
for i in range(len(s)//2):
    tmp+=s[i]+s[len(s)-i-1]
print(tmp)