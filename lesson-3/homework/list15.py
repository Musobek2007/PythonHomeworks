a=list(map(int,input().split()))
b=0
for i in a:
    b+=1-i%2
print(b)