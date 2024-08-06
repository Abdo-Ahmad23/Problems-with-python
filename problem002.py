import sys
import math

sum=0
cnt=0
for i in range(10):
    numbers =  int(input())
    if(numbers%2==0):
        sum+=numbers
        cnt+=1
if(cnt==0):
    print('No even numbers were entered.')
elif(sum/cnt==(int(sum/cnt))):
    print(f'The average of the even numbers is: {int(sum/cnt)}')
else:
    print(f'The average of the even numbers is: {sum/cnt}')

