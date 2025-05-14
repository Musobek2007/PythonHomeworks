a={}
while 1:
    b=input().split()
    if len(b)==0:
        break
    else:
        a[b[1]]=b[0]
print(a)