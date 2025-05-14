a=[]
while 1:
    b=input().split()
    if len(b)==0:
        break
    else:
        a+=[[b[0],b[1]]]
a.sort(key=lambda x:x[0])
d={}
for j in a:
    d[j[0]]=j[1]
print(d)