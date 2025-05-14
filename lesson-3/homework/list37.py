a=list(map(int,input().split()))
b=0
for i in a:
    if i<0:b+=i
print(b)