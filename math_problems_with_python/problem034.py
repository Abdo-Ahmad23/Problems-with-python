import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
m = int(input())
n = int(input())
tmp=''
tmp_l=l
for i in range(n):
    tmp+=str(tmp_l)+' '
    tmp_l+=m
print(tmp[:-1])
tmp=''
for i in range(n):
    tmp+=str(l)+' '
    l//=m
print(tmp[:-1])
