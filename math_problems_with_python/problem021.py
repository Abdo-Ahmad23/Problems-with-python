import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
n = int(input())
tmp=''
for i in range(n):
    x = input()
    x=x.replace(s,'')
    tmp+=x
print(tmp)

