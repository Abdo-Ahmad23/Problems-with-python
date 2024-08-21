import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()
letter = input()

if letter.isupper():
    print(message[ord(letter)-ord('A')])
else:
    print(message[ord(letter)-ord('a')])

