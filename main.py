import random

def swap_characters(s, i, j):
    # Convert the string to a list of characters
    s=sorted(s)
    # print(f's={s}')
    char_list = list(s)
    
    # Perform the swap
    char_list[i], char_list[j] = char_list[j], char_list[i]
    
    # Join the list back into a string
    swapped_string = ''.join(char_list)
    print(swapped_string)
    
    return swapped_string
def check(s):
    s=sorted(s)
    if(s[0]==s[-1]):
        return False
    return True

t=int(input())
for _ in range(t):
    s=input()
    if(check(s)):
        print('YES')
        print(swap_characters(s,0,-1))
        # print(s)
    else:
        print("NO")
    