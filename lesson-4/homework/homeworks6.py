m=100
s=[1]*(m+1)
s[0]=0
s[1]=0
for i in range(2,m):
    if s[i]:
        for j in range(i*i,m,i):
            s[j]=0
for p in range(2,100):
    if s[p]:
        print(p,end=' ')