import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
m = input()

dots=len(s)-1

if m=='|':
    print(s[::-1])
elif m=='\\':
    s=s[::-1]
    for i in range(len(s)):
        tmp=''
        for j in range(dots):
            tmp+='.'
        tmp+=s[i]
        print(tmp)
        dots-=1
else:
    s=s[::-1]
    for i in range(len(s)):
        tmp=''
        for j in range(i):
            tmp+='.'
        tmp+=s[i]
        print(tmp)
        # dots-=1
