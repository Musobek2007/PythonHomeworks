a=input().split()
b=[]
for i in a:
    if i not in b:
        b+=[i]
print(b)