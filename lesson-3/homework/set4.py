a=set(map(int,input().split()))
b=set(map(int,input().split()))
a=list(a)
b=list(b)
f=False
n=len(a)
k=len(b)
for i in range(n-k+1):
    if a[i:i+k]==b:
        f=True
        break
for i in range(k-n+1):
    if b[i:i+n]==a:
        f=True
        break
print(f)