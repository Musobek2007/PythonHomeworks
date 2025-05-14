a={}
c=[]
while 1:
    b=input().split()
    if len(b)==1:
        break
    else:
        a[b[0]]=b[1]
for i,j in a.items():
    if j==b[0]:
        c+=[i]
print(c)
