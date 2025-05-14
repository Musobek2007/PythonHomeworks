a=list(map(int,input().split()))
b=int(input())
c=[]
for i in range(len(a)):
    if a[i]==b:
        c+=[i]
print(c)