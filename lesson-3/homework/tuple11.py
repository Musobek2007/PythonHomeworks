a=tuple(map(int,input().split()))
b=int(input())
s=[]
for i in range(len(a)):
    if a[i]==b:
        s+=[i]
print(s)