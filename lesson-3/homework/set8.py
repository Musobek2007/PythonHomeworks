a=set(map(int,input().split()))
b=int(input())
if b in a:
    a.remove(b)
print(a)