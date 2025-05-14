a={}
while 1:
    b=input().split()
    if len(b)==1:
        break
    else:
        a[b[0]]=b[1]
if b[0] in a:print(b[0],a[b[0]])
else:print('no')