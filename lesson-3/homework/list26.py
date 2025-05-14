a=list(map(int,input().split()))
n=len(a)
if n%2:
    print(a[n//2])
else:print(a[n//2-1:n//2+1])