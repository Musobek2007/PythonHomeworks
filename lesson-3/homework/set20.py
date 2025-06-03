a=set(map(int,input().split()))
b=set(map(int,input().split()))
c=a&b
if not c:print(True)
else:print(False)