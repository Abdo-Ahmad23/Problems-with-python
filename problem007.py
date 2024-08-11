def sort_substring(s, i, j):
    i-=1
    j-=1
    # Extract the part before, the part to be sorted, and the part after
    before = s[:i]
    to_sort = s[i:j+1]
    after = s[j+1:]
    
    # Sort the substring
    sorted_substring = ''.join(sorted(to_sort))
    
    # Combine the parts back into the full string
    result = before + sorted_substring + after
    
    return result

def reverse_substring(s, i, j):
    i-=1
    j-=1
    # Extract the part before, the part to be reversed, and the part after
    before = s[:i]
    to_reverse = s[i:j+1]
    after = s[j+1:]
    
    # Reverse the substring
    reversed_substring = to_reverse[::-1]
    
    # Combine the parts back into the full string
    result = before + reversed_substring + after
    
    return result

def get_substring(s, i, j):
    i-=1
    j-=1
    # Extract the substring from index i to j (inclusive)
    substring = s[i:j+1]
    return substring
print(reverse_substring('54321',1,3))
nn=input().split()
n=int(nn[0])
q=int(nn[1])
s=input()
for _ in range(q):
    string=input().split()
    if string[0]=='substr':
        print(get_substring(s,int(string[1]),int(string[2])))
    if string[0]=='sort':
        s=sort_substring(s,int(string[1]),int(string[2]))
    if string[0]=='pop_back':
        s=s[:-1]
    if string[0]=='front':
        print(s[0])
    if string[0]=='back':
        print(s[-1])
    if string[0]=='reverse':
        s=reverse_substring(s,int(string[1]),int(string[2]))
    if string[0]=='print':
        print(s[int(string[1])-1])
    elif string[0]=='push_back':
        s+=string[1]

