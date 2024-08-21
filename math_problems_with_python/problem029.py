import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s1 = input().split()
s2 = input().split()
s1.sort()
tmp=''
for i in s1:
    if i in s2 and i!=' ':
        tmp+=i+' '

print(tmp[:-1])