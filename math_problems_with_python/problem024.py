import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()

s=sorted(s)
f=int(s[0])
l=int(s[-2])
cnt=0
for i in range(f,l):
    if s[cnt]!=str(i):
        print(i)
        break
    cnt+=1
