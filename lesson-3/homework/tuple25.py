a=tuple(map(int,input().split()))
b=[]
for i in a:
    if i not in b:
        b+=[i]
b=tuple(b)
print(b)