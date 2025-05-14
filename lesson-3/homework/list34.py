a=list(map(int,input().split()))
for i in range(2):
    a=[a[-1]]+a[:-1]
print(a)
