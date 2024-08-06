import sys
import math
import string
import re

def extract_punctuation_and_alpha(s):
    result = []
    for char in s:
        if char in string.punctuation or char.isalpha():
            result.append(char)
    return ''.join(result)

# print(extract_punctuation_and_alpha('kjkj!!!78'))
def split_string_on_multiple(s, delimiters):
    # Create a regular expression pattern for the delimiters
    pattern = f"[{re.escape(delimiters)}]"
    return re.split(pattern, s)


s=input()#12a13b
numbers=split_string_on_multiple(s, extract_punctuation_and_alpha(s))
numbers.pop()
characters=[]
for i in range(len(s)):
    if(not s[i].isdigit()):
        characters.append(s[i])
tmp=''
for i in range(len(numbers)):
    tmp+= characters[i] * int(numbers[i])
    

print(tmp)