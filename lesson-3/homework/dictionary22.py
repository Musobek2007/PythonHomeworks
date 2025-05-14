a={}
while 1:
    b=input().split()
    if len(b)==0:
        break
    else:
        a[b[0]]=int(b[1])
f={i:j for i,j in a.items() if j>10}
print(f)