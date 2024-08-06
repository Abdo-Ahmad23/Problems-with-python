import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

first_name = input()
first_health = int(input())
first_attack = int(input())
second_name = input()
second_health = int(input())
second_attack = int(input())
if(first_health+first_attack==second_attack+second_health):
    print('Draw')
elif(first_health+first_attack>second_attack+second_health):
    print(first_name)
else:
    print(second_name)


