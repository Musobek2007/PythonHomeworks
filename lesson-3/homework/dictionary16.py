a={}
while 1:
    b=input().split()
    if len(b)==0:
        break
    else:
        a[b[0]]=b[1]
f=False
for i,j in a.items():
    if j in a:
        f=True
print(f)