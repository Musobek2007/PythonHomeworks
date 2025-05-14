a=tuple(map(int,input().split()))
c=tuple(a[i:i+4] for i in range(0,len(a),4))
print(c)