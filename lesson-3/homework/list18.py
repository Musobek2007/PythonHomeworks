a=list(map(int,input().split()))
b=list(map(int,input().split()))
n=len(a)
k=len(b)
f=False
for i in range(n-k+1):
    if a[i:i+k]==b:
        f=True
        break
print(f)