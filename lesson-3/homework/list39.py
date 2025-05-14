a=list(map(int,input().split()))
c=[]
for j in range(0,len(a),3):
    c+=[a[j:j+3]]
print(c)