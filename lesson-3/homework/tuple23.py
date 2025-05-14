a=tuple(map(int,input().split()))
p=tuple(a[i] for i in range(len(a)-1,-1,-1))
print(p)