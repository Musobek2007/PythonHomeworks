a={}
c=set()
while 1:
    b=input().split()
    if len(b)==0:
        break
    else:
        a[b[0]]=b[1]
        c.add(b[1])
print(len(c))
