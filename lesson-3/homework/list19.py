a=list(map(int,input().split()))
b=int(input())
for i in range(len(a)):
    if a[i]==b:
        a[i]=b-1
        break
print(a)