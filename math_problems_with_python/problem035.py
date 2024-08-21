a,b,c,d=map(int,input().split())
ok=0
if a+b+c==d:
    ok=1
elif a + b - c == d:
    ok = 1
elif a + b * c == d:
    ok = 1

elif a-b-c==d:
    ok=1
elif a - (b + c == d:
    ok = 1
elif a - (b * c) == d:
    ok = 1

elif (a * b) + c == d:
    ok = 1
elif (a * b) - c == d:
    ok = 1
elif a * b * c == d:
    ok = 1

if ok:
    print("YES")
else:
    print("NO")

print(a*b*c+982)