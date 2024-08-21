import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w = input()
c = input()

res = list()
ok = 0
for i in range(len(w)):
    if ok:
        res.append(w[::-1])
        ok = 0
    else:
        res.append(w)
        ok = 1

if c == 'S':
    print(' '.join(res))
else:
    print('\n'.join(res))

