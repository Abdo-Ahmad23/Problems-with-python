import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
c = input()
tmp=''
for i in s:
    if i.isdigit():
        tmp+=i
print(c.join(tmp))
